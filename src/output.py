# Everyone
from pathlib import Path
from src.metric import MetricRecord

dir_path = Path(__file__).parent.resolve()
data_file = f'{dir_path}\data.csv'


class OutputController:
  """Controller that manages data collected being saved to local files\n
  Data should be saved on collection such that an unexpected error will
  not destroy all previously collected data

  :param con: Reference to main controller
  :type con: main.Controller
  """

  FILENAME = 'data.csv'

  def __init__(self, con):
    self.con = con

  def record_results(self, data: list[MetricRecord]):
    """Records a result and saves it to the current records file

    :param data: Data to record
    """
    pass
