# Egor and Stepan
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

  def measure_value(self) -> float:
    with PiCamera() as camera:
      # Use https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.capture
      # camera.capture('temp.jpg')
      # TODO: Open the file and read the light intensity of the pixels
      # Use a func to get average intensity (From 0 -> 1) from a grid section of the image
      # Return a tuple of the average insensity of each section
      return (1, 1, 1, 1)

  def check_deviance(self, new_value: tuple) -> bool:
    if len(self.history) < 3:
      return False

    averages = ((x + y + z) / 3 for x, y, z in zip(*self.history[-3:]))
    differences = (abs(n - o) for n, o in zip(new_value, averages))
    return any((d >= self.deviance_value for d in differences))
