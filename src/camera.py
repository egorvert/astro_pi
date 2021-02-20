###########################################################
##   Code relating to the PiCamera module is untested    ##
##   due to our team not having access to the testing    ##
##   RaspberryPi. Therefore it would be appreciated if   ##
##     this could be taken into consideration during     ##
##  testing phases. Thanks from the underscore team. :)  ##
###########################################################

import numpy as np

from src.metric import MetricController

try:
  from picamera import PiCamera
  test_camera = False
except:
  # If this fails then that likely means it is not running on
  # the raspberry pi. Therefore import the local testing version
  print('\033[33m' + '⚠️  WARNING: Using local test version of PiCamera ⚠️')
  print('⚠️  WARNING: Do not take results as example data  ⚠️\n' + '\033[0m')
  from src.test_modules import PiCamera
  test_camera = True


class CameraController(MetricController):
  """Controller for methods and data related to the light sensor/camera.
  Inherits from the ``MetricController`` class.
    
  :param con: Reference to main controller
  :type con: main.Controller
  """
  def __init__(self, con):
    super().__init__(0.1, 'camera')
    self.con = con
    self.sense = con.sense
    self.testing = test_camera

    self.w = 640
    self.h = 480

    # Divisions are the number of sections to split the image into for separate
    # intensity values. E.g.: 3 would cause it to be cut into a 3x3 grid
    self.divisions = 2

  @property
  def gridw(self):
    return int(self.w / self.divisions)

  @property
  def gridh(self):
    return int(self.h / self.divisions)

  def measure_value(self) -> tuple[float]:
    """Captures an image from the connected camera, cuts it into a grid like layout,
    and returns the average light intensities of each grid square.

    :return: A tuple of intensity values ranging from 0 to 1
    :rtype: tuple[float]
    """
    with PiCamera(resolution=(self.w, self.h)) as camera:
      pixels = np.empty((self.h, self.w, 3), dtype=np.uint8)
      camera.capture(pixels, 'rgb')
      return self.fragment_pixels(pixels)

  def fragment_pixels(self, pixels: np.ndarray) -> list[float]:
    """Breaks up a large 3d array into a grid like layout and returns the average
    intensities of each grid square.

    :param pixels: A 3d numpy array of dimensions: width, height, 3 (for RGB values)
    :type pixels: np.ndarray
    :return: An array of intensities ranging from 0 to 1
    :rtype: list[float]
    """
    intensities = []
    for i in range(0, self.h, self.gridh):
      for j in range(0, self.w, self.gridw):
        height_slice = pixels[i:i + self.gridh]
        width_slice = map(lambda x: x[j:j + self.gridw], height_slice)
        intensity = self.calc_average_intensity(width_slice)
        intensities.append(intensity)
    return intensities

  def calc_average_intensity(self, section) -> float:
    """Calculates the average light intensity of a 3d array.

    :param section: A 3d numpy array of dimensions: width, height, 3 (for RGB values)
    :type section: np.ndarray
    :return: The average light intensity
    :rtype: float
    """
    flat_list = [item for sublist in section for item in sublist]
    intensities = [sum(rgb) / (255 * 3) for rgb in flat_list]
    return sum(intensities) / len(intensities)

  def check_deviance(self, new_value: tuple[float]) -> bool:
    """Calculates whether there was a deviance in light intensity of any
    of the grid squares.

    :param new_value: The new list of intensities
    :type new_value: tuple[float]
    :return: Whether there was a deviance in intensities
    :rtype: bool
    """
    if len(self.history) < 3:
      return False

    averages = ((x + y + z) / 3 for x, y, z in zip(*self.history[-3:]))
    differences = (abs(n - o) for n, o in zip(new_value, averages))
    return any((d >= self.deviance_value for d in differences))
