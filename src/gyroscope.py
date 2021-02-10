# Adam and Ben
from metric import MetricController

class GyroscopeController(MetricController):
  """
    Controller for methods and data related to the gyroscope
    
    :param con: Reference to main controller
    :type con: main.Controller
  """
  def __init__(self, con):
    self.con = con
