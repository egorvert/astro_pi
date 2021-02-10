class MetricController:
  def __init__(self, deviance_value):
    self.history = []
    self.deviance_value = deviance

  def get_timestamp(self):
    pass

  def measure_value(self):
    # Nothing will go here as it is meant to be rewritten
    # by the classes that inherit this as they will be getting new values
    # via different methods
    return 0

  def check_deviance(self, new_value):
    # Works out the average from the past three results stored in history
    # Subtracts the current result from the average
    # Checks whether the deviance is significant (if it is greater than self.deviance_value)
    # If it is - return True
    # Else - False
    pass

  def measure(self):
    new_value = self.measure_value()
    info = {
        'time': self.get_timestamp(),
        'value': new_value,
        'is_deviant': self.check_deviance(new_value)
    }
    self.history.push(new_value)
    return info
