import random


def rand():
  return random.random() * 2 - 1


class SenseHat:
  def __init__(self):
    pass

  def _get_xyz(self):
    return { 'x': rand(), 'y': rand(), 'z': rand() }

  def get_gyroscope_raw(self):
    return self._get_xyz()

  def get_accelerometer_raw(self):
    return self._get_xyz()
