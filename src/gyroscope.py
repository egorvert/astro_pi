# Adam and Ben
from src.metric import MetricController


class GyroscopeController(MetricController):
  """Controller for methods and data related to the gyroscope
  
  :param con: Reference to main controller
  :type con: main.Controller
  """
  def __init__(self, con):
    super().__init__(1, 'gyroscope')
    self.con = con

  def measure_value(self):
    # Reads the value from the relevent module and returns it
    return 1
