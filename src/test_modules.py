import os
import random
from pathlib import Path

import numpy as np
from PIL import Image

try:
  import requests
except:
  requests = None


def rand():
  return random.random() * 2 - 1


def randstr():
  return str(random.random())[3:]


class SenseHat:
  def __init__(self):
    pass

  def _get_xyz(self):
    return { 'x': rand(), 'y': rand(), 'z': rand() }

  def get_gyroscope_raw(self):
    return self._get_xyz()

  def get_accelerometer_raw(self):
    return self._get_xyz()

  def load_image(self, file_path, redraw=True):
    pass


class PiCamera:
  def __init__(self, resolution: tuple = (640, 480)):
    self.resolution = resolution

  def __enter__(self):
    return self

  def __exit__(self, type, value, traceback):
    pass

  def capture(self, output, *args, **kwargs):
    if requests is None:
      output.fill(0)
      return

    Path("temp/img").mkdir(parents=True, exist_ok=True)

    filename = f'temp/img/{randstr()}.jpg'
    with open(filename, 'wb') as f:
      w, h = self.resolution
      res = requests.get(f'https://picsum.photos/{w}/{h}.jpg')
      f.write(res.content)

    im = Image.open(filename)
    pixels = np.array(im)
    output.fill(0)
    output += pixels

    os.remove(filename)
