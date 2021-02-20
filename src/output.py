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

  def log(self, message: str, err: Exception = None, show_stdout: bool = True):
    """Adds a record to the outputted csv file with the source type '*log*'
    Made to be easily called from other sections of the program.\n
    This method is *lazy*, meaning that it does not immediately write the the file.
    Instead, it adds it to a backlog and then these records are written to the file
    with the next batch of measurements. This prevents too many frequent file opens.

    :param message: The main message to record
    :type message: str
    :param err: An Exception to record with the message, defaults to None
    :type err: Exception, optional
    :param show_stdout: Whether to print the message in stdout as well as writing it to the output file, defaults to True
    :type show_stdout: bool, optional
    """
    if show_stdout:
      print(f'LOG: {message}', f'({type(err).__name__}: {str(err)})' if err is not None else '')
    record = MetricRecord(time=datetime.now(), source='log', value=message)
    if err is not None:
      record.error = err
    self.backlog.append(record)

  def record_results(self, data: list[MetricRecord]):
    """Records results and saves it to the current records file. Also writes the records stored in the backlog.

    :param data: The batch of records to record
    :type data: list[MetricRecord]
    """
    try:
      with open(OutputController.FILENAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(map(lambda r: r.csv_row, self.backlog + data))
    except Exception as err:
      self.log('Something went wrong recording the results', err)
      self.backlog += data
    else:
      self.backlog.clear()
