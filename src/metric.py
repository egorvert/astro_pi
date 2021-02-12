class MetricController:
  """Base class for controllers. Handles receiving data from hardware modules
  and analysing them for spikes in values.

  :param deviance_value: Minimum value that would count for a change
  :type deviance_value: float
  """
  def __init__(self, deviance_value: float):
    self.deviance_value = deviance_value

    self.history = []

  @staticmethod
  def get_timestamp():
    """Gets the current time"""
    return None

  def measure_value(self):
    # Nothing will go here as it is meant to be rewritten
    # by the classes that inherit this as they will be getting new values
    # via different methods
    return 0

  def check_deviance(self, new_value):
    """Compares a new value to the average of the previous values.\n
    If there is a notable deviance (Above self.deviance_value)

    :param new_value: The new value to check
    :type new_value: float
    :return: Whether the new value is deviant
    :rtype: bool
    """
    # Works out the average from the past three results stored in history
    # Subtracts the current result from the average
    # Checks whether the deviance is significant (if it is greater than self.deviance_value)
    # If it is - return True
    # Else - False
    pass

  def measure(self):
    new_value = self.measure_value()
    info = {
      'time': MetricController.get_timestamp(),
      'value': new_value,
      'is_deviant': self.check_deviance(new_value)
    }
    self.history.push(new_value)
    return info
