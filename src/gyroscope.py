from src.metric import MetricController


class GyroscopeController(MetricController):
  """
    Controller for methods and data related to the gyroscope
    
    :param con: Reference to main controller
    :type con: main.Controller
  """
  def __init__(self, con):
    super().__init__(1, 'gyroscope')
    self.con = con
    self.sense = con.sense

  def measure_value(self) -> tuple:
    values = self.sense.get_gyroscope_raw()
    return (values['x'], values['y'], values['z'])

  def check_deviance(self, new_value: tuple) -> bool:
    # TODO: This func takes in a tuple in 'new_value' and needs to return whether
    # it is deviant from the previous ones
    # To do this check it against the last few values in self.history (A list of the previous
    # tuples recorded)
    return False
