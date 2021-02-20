import os
import random
from pathlib import Path

import numpy as np
from PIL import Image

try:
  # Note: This code will not run on the Raspberry Pi in space,
  #       it is only here for testing purposes and the program
  #       will run perfectly fine with no requests module installed.
  import requests
except:
  requests = None


def rand():
  return random.random() * 2 - 1


def randstr():
  return str(random.random())[3:]


class SenseHat:
  """Simulates the functions from the SenseHat module by
  supplying random data. Allows the program to run in a testing
  environment.
  """
  def __init__(self):
    pass

  def _get_xyz(self) -> tuple[float]:
    """Generates a tuple of 3 random numbers between -1 and 1"""
    return { 'x': rand(), 'y': rand(), 'z': rand() }

  def get_gyroscope_raw(self) -> tuple[float]:
    """Generates simulated gyroscope data"""
    return self._get_xyz()

  def get_accelerometer_raw(self) -> tuple[float]:
    """Generates simulated accelerometer data"""
    return self._get_xyz()

  def load_image(self, file_path, redraw=True):
    """Simulates loading an image into the LED matrix. Actually does nothing"""
    pass


class PiCamera:
  """Simulates the functions from the PiCamera module by
  supplying mimic data in place of real input. Allows the
  program to run in a testing environment.

  :param resolution: A tuple with the width and height of the image to request
  """
  def __init__(self, resolution: tuple = (640, 480)):
    self.resolution = resolution

  def __enter__(self):
    """Allows the class to be used in a `with` block"""
    return self

  def __exit__(self, type, value, traceback):
    """Allows the class to be used in a `with` block"""
    pass

  def capture(self, output: np.ndarray, *args, **kwargs):
    """Simulates getting an image output from the onboard camera.\n
    Works by requesting a random image from the website `https://picsum.photos`.

    :param output: A numpy array with the same dimensions as the image requested
    """
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
