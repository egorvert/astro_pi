# Egor and Stepan
from metric import MetricController
class CameraController(MetricController):
  """
    Controller for methods and data related to the light sensor/camera.
    
    :param con: Reference to main controller
    :type con: main.Controller
  """
  def __init__(self, con):
    self.con = con

  def recordResults(self):
      pass
