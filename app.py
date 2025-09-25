import datetime
import io

from astral.geocoder import database, lookup
from astral.sun import dawn, sunrise
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from font_fredoka_one import FredokaOne
from PIL import Image, ImageDraw, ImageFont

app = FastAPI()


def user_timezone():
  """TODO(HACK) just hardcoding for me"""
  return datetime.timezone(datetime.timedelta(hours=-8))


def user_image_dimensions():
  """TODO(HACK) Return image dimensions for my phone"""
  return 368, 122


def get_sunrise_times():
  """Return dawn and sunrise times"""
  location = lookup("San Francisco", database())
  utc_time = dawn(location.observer, datetime.date.today())
  sunrise_time = sunrise(location.observer, datetime.date.today())
  return utc_time.astimezone(user_timezone()), sunrise_time.astimezone(user_timezone())


def generate_weather_image():
  """Generate the weather image and return as bytes"""
  dawn_time, sunrise_time = get_sunrise_times()
  
  width, height = user_image_dimensions()
  image = Image.new("RGB", (width, height), "white")
  
  draw = ImageDraw.Draw(image)
  text = f"dawn {dawn_time.strftime('%H:%M')}\nsunrise {sunrise_time.strftime('%H:%M')}"
  
  font_size = int(height * 0.45)
  font = ImageFont.truetype(FredokaOne, font_size)
  
  draw.text((width // 2, height // 2), text, fill="black", font=font, anchor="mm")
  
  img_buffer = io.BytesIO()
  image.save(img_buffer, format="PNG")
  img_buffer.seek(0)
  
  return img_buffer


@app.get("/render")
async def render_weather_image(request: Request):
  """HTTP endpoint to render and return the weather image"""

  
  print("Request headers:")
  for header_name, header_value in request.headers.items():
    print(f"  {header_name}: {header_value}")

  img_buffer = generate_weather_image()
  
  return StreamingResponse(
    io.BytesIO(img_buffer.read()),
    media_type="image/png",
    headers={"Content-Disposition": "inline; filename=weather.png"}
  )

if __name__ == "__main__":
  """For local development"""
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)
