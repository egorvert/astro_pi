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
    
  :param con: Reference to main controller
  :type con: main.Controller
  """
  def __init__(self, con):
    super().__init__(0.1, 'camera')
    self.con = con
    self.sense = con.sense
    self.testing = test_camera

    # Divisions are the number of sections to split the image into for separate
    # intensity values. E.g.: 3 would cause it to be cut into a 3x3 grid
    self.divisions = 4

  def measure_value(self) -> tuple[float]:
    with PiCamera(resolution=(640, 480)) as camera:
      pixels = np.empty((480, 640, 3), dtype=np.uint8)
      camera.capture(pixels, 'rgb')
      # TODO: Split the pixels into equal sections based on self.divisions
      # TODO: Calculate intensity of each section with self.calc_average_intensity()
    return (1, 1, 1, 1)  # TODO: Return tuple of intensities

  def calc_average_intensity(self, section: np.ndarray) -> float:
    return 1  # TODO: Calculate the average intensity of the array

  def check_deviance(self, new_value: tuple[float]) -> bool:
    if len(self.history) < 3:
      return False

    averages = ((x + y + z) / 3 for x, y, z in zip(*self.history[-3:]))
    differences = (abs(n - o) for n, o in zip(new_value, averages))
    return any((d >= self.deviance_value for d in differences))
