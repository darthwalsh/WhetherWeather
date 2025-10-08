import datetime
import io
import logging  # MAYBE need to configure logging, maybe allow header or param to set log level
from zoneinfo import ZoneInfo

from astral.geocoder import database, lookup
from astral.sun import dawn, sunrise
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from font_fredoka_one import FredokaOne
from PIL import Image, ImageDraw, ImageFont
from pydantic import BaseModel

app = FastAPI()


class Config(BaseModel):
  """Configuration settings for the weather app"""
  timezone: str
  image_dim: tuple[int, int]
  location: str
  

def get_config():
  """Return the application configuration
     TODO(HACK) just hardcoding for me"""
  return Config(
    timezone="America/Los_Angeles",
    image_dim=(368, 122),
    location="San Francisco",
  )


def get_sunrise_times():
  """Return dawn and sunrise times"""
  config = get_config()
  location = lookup(config.location, database())

  utc_time = dawn(location.observer, datetime.date.today())
  sunrise_time = sunrise(location.observer, datetime.date.today())

  timezone = ZoneInfo(config.timezone)
  return utc_time.astimezone(timezone), sunrise_time.astimezone(timezone)


def generate_weather_image():
  """Generate the weather image and return as bytes"""
  config = get_config()
  dawn_time, sunrise_time = get_sunrise_times()
  
  width, height = config.image_dim
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
  logging.debug("Request headers:")
  for header_name, header_value in request.headers.items():
    logging.debug(f"  {header_name}: {header_value}")

  # MAYBE should set cache headers?

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
