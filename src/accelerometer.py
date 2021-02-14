# Greg and Alan
from sense_hat import SenseHat
from src.metric import MetricController


class AccelerometerController(MetricController):
  """Controller for methods and data related to the accelerometer

  :param con: Reference to main controller
  :type con: main.Controller
  """
  def __init__(self, con):
    super().__init__(1, 'accelerometer')
    self.con = con

  def measure_value(self):
    # Reads pitch, raw, yaw and return tuple (x, y, z)
    sense = SenseHat()
    accel_value = sense.get_accelerometer_raw()
    x = accel_value.get('x')
    y = accel_value.get('y')
    z = accel_value.get('z')
    accel =(x, y, z)

    return accel

  def check_deviance(self, new_value: tuple) -> bool:

    return True
