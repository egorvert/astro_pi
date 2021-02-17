import time
from datetime import datetime, timedelta

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
  print('⚠️  WARNING: Do not take results as example data  ⚠️\n' + '\033[0m')
  from src.test_modules import SenseHat
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

  def begin_experiment(self, framerate: int = 10, measure_period: int = 5, duration: int = 178):
    """Handles the main loop of the experiment. Calls all components
    and directs their results to the output controller
    """
    print('Ooga booga im in space')
    framecount = 0
    end_time = datetime.now() + timedelta(minutes=duration)
    while datetime.now() < end_time:
      self.light_matrix.update()

      if framecount % (framerate * measure_period) == 0:
        minutes = (end_time - datetime.now()).total_seconds() // 6 / 10
        print(f'Measuring sensors... ({minutes} min{"s"[minutes==1:]} remaining)')
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

  if main.testing:
    main.output.log('SenseHat could not be accessed -> Using dummy module', show_stdout=False)
  if main.camera.testing:
    main.output.log('PiCamera could not be accessed -> Using dummy module', show_stdout=False)

  poststr = ' in testing mode' if main.testing or main.camera.testing else ''
  main.output.log('Experiment beginning' + poststr)

  try:
    main.begin_experiment()
  except Exception as err:
    main.output.log('Experiment ceased unexpectedly', err)
  except KeyboardInterrupt:
    main.output.log('Experiment halted manually')
  else:
    main.output.log('Experiment has completed successfully')
  finally:
    main.output.log('Experiment has stopped')
    main.output.record_results([])
