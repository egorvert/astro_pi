import csv
from datetime import datetime
from src.metric import MetricRecord


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
    self.backlog = []

  def log(self, message: str, err: Exception = None):
    print(f'LOG: {message}', f'({type(err).__name__}: {str(err)})' if err is not None else '')
    record = MetricRecord(time=datetime.now(), source='log', value=message)
    if err is not None:
      record.error = err
    self.backlog.append(record)

  def record_results(self, data: list[MetricRecord]):
    """Records a result and saves it to the current records file

    :param data: Data to record
    """
    with open(OutputController.FILENAME, 'a', newline='') as f:
      writer = csv.writer(f)
      writer.writerows(map(lambda r: r.csv_row, self.backlog + data))
    self.backlog.clear()
