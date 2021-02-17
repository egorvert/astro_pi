# Egor and Stepan
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

    # Divisions are the number of sections to split the image into for separate
    # intensity values. E.g.: 3 would cause it to be cut into a 3x3 grid
    self.divisions = 4

  def capture(self):  #this needs to be done for example every 5 seconds
    i = 1  #this should be put in the main loop
    #2 different arrays to capture 2 frames in so that they can be compared
    output1 = np.empty((480, 640, 3), dtype=np.uint8)
    #this sould stay out of the main loop so that they are only made once
    output2 = np.empty((480, 640, 3), dtype=np.uint8)
    camera.capture_effects = (128.128)
    camera.resolution = (640, 480)
    if i % 2 != 0:
      camera.capture(output1, 'rgb')
    else:
      camera.capture(output2, 'rgb')

    if i % 2 == 0:
      differences = np.subtract(output2, output1)
      print(differences)
    elif i % 2 != 0 and i != 1:
      differences = np.subtract(output1, output2)
    i += 1
    sleep(5)  #captures 2 frames 5 seconds apart
    camera.close()

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
