from src.metric import MetricController


class GyroscopeController(MetricController):
  """
    Controller for methods and data related to the gyroscope.
    Inherits from the ``MetricController`` class.
    
    :param con: Reference to main controller
    :type con: main.Controller
  """
  def __init__(self, con):
    dev = (2 * 3**0.5) * (0.3 if con.testing else 0.05)
    super().__init__(dev, 'gyroscope')
    self.con = con
    self.sense = con.sense

  def measure_value(self) -> tuple:
    values = self.sense.get_gyroscope_raw()
    return (values['x'], values['y'], values['z'])
