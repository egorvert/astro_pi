from src.accelerometer import AccelerometerController
from src.camera import CameraController
from src.gyroscope import GyroscopeController
from src.light_matrix import MatrixController
from src.output import OutputController


class Controller:
  """Controller for top-level management of the experiment\n
  It separates out the smaller modules and gives them access to other modules
  Only big-picture experiment administration should be put here
  """
  def __init__(self):
    self.output = OutputController(self)
    self.camera = CameraController(self)
    self.accelerometer = AccelerometerController(self)
    self.gyroscope = GyroscopeController(self)
    self.light_matrix = MatrixController(self)

  def begin_experiment(self):
    """Handles the main loop of the experiment. Calls all components
    and directs their results to the output controller
    """
    print('Ooga booga im in space')


if __name__ == '__main__':
  main = Controller()
  main.output.log('Experiment has begun')
  try:
    main.begin_experiment()
  except Exception as err:
    main.output.log('Experiment ceased unexpectedly', err)
  else:
    main.output.log('Experiment has completed successfully')
  finally:
    main.output.log('Experiment has stopped')
    main.output.record_results([])
