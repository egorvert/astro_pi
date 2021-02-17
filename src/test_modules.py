import random, requests


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

  def set_rotation(self, *args, **kwargs):
    pass

  def show_message(self, *args, **kwargs):
    pass

  def set_pixels(self, *args, **kwargs):
    pass

  def load_image(self, file_path, redraw=True):
    pass


class PiCamera:
  def __init__(self):
    pass

  def __enter__(self):
    return PiCamera()

  def __exit__(self, type, value, traceback):
    pass

  def capture(self, output, *args, **kwargs):
    with open(output, 'wb') as f:
      res = requests.get('https://picsum.photos/400.jpg')
      f.write(res.content)
