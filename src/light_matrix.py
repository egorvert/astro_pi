# Egor and Stepan
from metric import MetricController

class MatrixController(MetricController):
  """
    Controller for methods and data related to the light matrix

    :param con: Reference to main controller
    :type con: main.Controller
  """
  def __init__(self, con):
    self.con = con
