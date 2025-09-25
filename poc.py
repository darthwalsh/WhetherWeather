import datetime

from astral.geocoder import database, lookup
from astral.sun import dawn, sunrise
from font_fredoka_one import FredokaOne
from PIL import Image, ImageDraw, ImageFont


def user_timezone():
  """TODO(HACK) just hardcoding for me"""
  return datetime.timezone(datetime.timedelta(hours=-8))


def user_image_dimensions():
  """TODO(HACK) Return image dimensions for my phone"""
  return 600, 200


def sunrise_time():
  """Return dawn and sunrise times"""
  location = lookup("San Francisco", database())
  utc_time = dawn(location.observer, datetime.date.today())
  sunrise_time = sunrise(location.observer, datetime.date.today())
  return utc_time.astimezone(user_timezone()), sunrise_time.astimezone(user_timezone())


dawn_time, sunrise_time = sunrise_time()

width, height = user_image_dimensions()
image = Image.new("RGB", (width, height), "white")

draw = ImageDraw.Draw(image)
text = f"dawn {dawn_time.strftime('%H:%M')}\nsunrise {sunrise_time.strftime('%H:%M')}"

font_size = int(height * 0.4)
font = ImageFont.truetype(FredokaOne, font_size)

draw.text((width // 2, height // 2), text, fill="black", font=font, anchor="mm")

image.save("render.png")
