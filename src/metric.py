from dataclasses import dataclass
from datetime import datetime


@dataclass
class MetricRecord:
  """Class that holds the information about a single point of data from a component"""
  time: datetime
  source: str
  value: float
  is_deviant: bool = False
  error: Exception = None

  @property
  def csv_row(self) -> list:
    return [
      str(self.time), self.source,
      str(self.value), '1' if self.is_deviant else '0',
      f'{type(self.error).__name__}: {str(self.error)}'
      if self.error is not None else ''
    ]


class MetricController:
  """Base class for controllers. Handles receiving data from hardware modules
  and analysing them for spikes in values.

  :param deviance_value: Minimum value that would count for a change
  """
  def __init__(self, deviance_value: float, source: str):
    self.deviance_value = deviance_value
    self.source = source
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
    if len(self.history) < 3:
      return False

    average = sum(self.history[-3:]) / 3
    return abs(new_value - average) >= self.deviance_value

  def measure(self) -> MetricRecord:
    """Reads a new data point from the component and returns
    it paird with metadata about the record"""
    try:
      value = self.measure_value()
      is_deviant = self.check_deviance(value)
      self.history.push(value)
      error = None
    except Exception as err:
      value = 0
      error = err
      is_deviant = False
    return MetricRecord(time=datetime.now(),
                        source=self.source,
                        value=value,
                        is_deviant=is_deviant,
                        error=error)
