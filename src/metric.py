from dataclasses import dataclass
from datetime import datetime


@dataclass
class MetricRecord:
  """Class that formats a group of information into a row to write to the output csv file"""
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
      f'{type(self.error).__name__}: {str(self.error)}' if self.error is not None else ''
    ]


class MetricController:
  """Base class for controllers. Handles receiving data from hardware modules
  and analysing them for spikes in values.

  :param deviance_value: Minimum value that would count for a change
  :type deviance_value: float
  :param source: The name of the hardware component to label the row in the output
  :type source: str
  """
  def __init__(self, deviance_value: float, source: str = 'a sensor'):
    self.deviance_value = deviance_value
    self.source = source
    self.history = []

  def measure_value(self) -> float:
    """Reads a new value from the component"""
    # Nothing will go here as it is meant to be rewritten
    # by the classes that inherit this as they will be getting new values
    # via different methods
    return 0.0

  def check_deviance(self, new_value) -> bool:
    """Compares whether a new value has deviated from the previous records.
    Works with either a 3d vector or single numbers.

    :param new_value: The new value to check
    :return: Whether there was a deviance in values
    :rtype: bool
    """
    if len(self.history) < 3:
      return False

    t = type(new_value)
    if t == int or t == float:
      return self.check_deviance_number(new_value)
    if t == tuple or t == list:
      return self.check_deviance_tuple(new_value)
    return False

  def check_deviance_number(self, new_value: float) -> bool:
    """Compares a new value to the average of the previous values.\n
    If there is a notable deviance (Above self.deviance_value)

    :param new_value: A value to compare
    :type new_value: float
    :return: Whether there was a deviance in values
    :rtype: bool
    """
    average = sum(self.history[-3:]) / 3
    return abs(new_value - average) >= self.deviance_value

  def check_deviance_tuple(self, new_value: tuple[float]) -> bool:
    """Treats the new tuple as a 3d vector and compares it to the average of
    the previous 3 vectors. It then calculates the magnitude of the difference
    in these and returns whether this magnitude is significant.

    :param new_value: A 3d vector to compare
    :type new_value: tuple[float]
    :return: Whether there was a deviance in values
    :rtype: bool
    """
    old1, old2, old3 = self.history[-3:]
    average_old = ((o1 + o2 + o3) / 3 for o1, o2, o3 in zip(old1, old2, old3))
    difference = (n - o for n, o in zip(new_value, average_old))
    difference_mag = sum(map(lambda x: x**2, difference))**0.5
    return difference_mag >= self.deviance_value

  def measure(self) -> MetricRecord:
    """Reads a new data point from the component and returns
    it paird with metadata about the record
    
    :return: A record containing the data measured
    :rtype: MetricRecord
    """
    try:
      value = self.measure_value()
    except Exception as err:
      self.con.output.log('Something went wrong when measuring ' + self.source)
      value = 0
      error = err
      is_deviant = False
    else:
      is_deviant = self.check_deviance(value)
      self.history.append(value)
      error = None
    finally:
      return MetricRecord(
        time=datetime.now(), source=self.source, value=value, is_deviant=is_deviant, error=error
      )
