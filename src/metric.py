from dataclasses import dataclass
from datetime import datetime


@dataclass
class MetricRecord:
  """Class that holds the information about a single point of data from a component"""
  time: datetime
  value: float
  is_deviant: bool = False


class MetricController:
  """Base class for controllers. Handles receiving data from hardware modules
  and analysing them for spikes in values.

  :param deviance_value: Minimum value that would count for a change
  """
  def __init__(self, deviance_value: float):
    self.deviance_value = deviance_value
    self.history = []

  def measure_value(self) -> float:
    """Reads a new value from the component"""
    # Nothing will go here as it is meant to be rewritten
    # by the classes that inherit this as they will be getting new values
    # via different methods
    return 0.0

  def check_deviance(self, new_value: float) -> bool:
    """Compares a new value to the average of the previous values.\n
    If there is a notable deviance (Above self.deviance_value)

    :param new_value: The new value to check
    """
    average = sum(self.history[-3:]) / 3
    return abs(new_value - average) >= self.deviance_value

  def measure(self) -> MetricRecord:
    """Reads a new data point from the component and returns
    it paird with metadata about the record"""
    new_value = self.measure_value()
    info = MetricRecord(time=datetime.now(),
                        value=new_value,
                        is_deviant=self.check_deviance(new_value))
    self.history.push(new_value)
    return info
