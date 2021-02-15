import time
from sense_hat import SenseHat
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
    self.sense = SenseHat()

    self.output = OutputController(self)
    self.light_matrix = MatrixController(self)

    self.camera = CameraController(self)
    self.accelerometer = AccelerometerController(self)
    self.gyroscope = GyroscopeController(self)

  def begin_experiment(self, timegap=5):
    """Handles the main loop of the experiment. Calls all components
    and directs their results to the output controller
    """
    print('Ooga booga im in space')
    while True:
      cam_result = self.camera.measure()
      acc_result = self.accelerometer.measure()
      gyro_result = self.gyroscope.measure()
      self.light_matrix.update(cam_changed=cam_result.is_deviant,
                               acc_changed=acc_result.is_deviant,
                               gyro_changed=gyro_result.is_deviant)
      self.output.record_results([cam_result, acc_result, gyro_result])
      time.sleep(timegap)


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
