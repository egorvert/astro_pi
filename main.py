import time
from src.accelerometer import AccelerometerController
from src.camera import CameraController
from src.gyroscope import GyroscopeController
from src.light_matrix import MatrixController
from src.output import OutputController

try:
  from sense_hat import SenseHat
  testing = False
except:
  # If this fails then that likely means it is not running on
  # the raspberry pi. Therefore import the local testing version
  print('\033[33m' + '⚠️  WARNING: Using local test version of SenseHat ⚠️')
  print('⚠️  WARNING: Do not take results as example data  ⚠️' + '\033[0m')
  from src.test_sense_hat import SenseHat
  testing = True


class Controller:
  """Controller for top-level management of the experiment\n
  It separates out the smaller modules and gives them access to other modules
  Only big-picture experiment administration should be put here
  """
  def __init__(self):
    self.sense = SenseHat()
    self.testing = testing

    self.output = OutputController(self)
    self.light_matrix = MatrixController(self)

    self.camera = CameraController(self)
    self.accelerometer = AccelerometerController(self)
    self.gyroscope = GyroscopeController(self)

  def begin_experiment(self, framerate: int = 10, measure_period: int = 5):
    """Handles the main loop of the experiment. Calls all components
    and directs their results to the output controller
    """
    print('Ooga booga im in space')
    framecount = 0
    while True:
      self.light_matrix.update()

      if framecount % (framerate * measure_period) == 0:
        print('Measuring sensors...')
        cam_result = self.camera.measure()
        acc_result = self.accelerometer.measure()
        gyro_result = self.gyroscope.measure()
        self.light_matrix.start_sequence(
          cam_changed=cam_result.is_deviant,
          acc_changed=acc_result.is_deviant,
          gyro_changed=gyro_result.is_deviant
        )
        self.output.record_results([cam_result, acc_result, gyro_result])

      framecount += 1
      time.sleep(1 / framerate)


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
