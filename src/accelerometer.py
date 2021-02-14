# Greg and Alan
from sense_hat import SenseHat
from src.metric import MetricController
from math import sqrt


class AccelerometerController(MetricController):
  """Controller for methods and data related to the accelerometer

  :param con: Reference to main controller
  :type con: main.Controller
  """
  def __init__(self, con):
    super().__init__(1, 'accelerometer')
    self.con = con

  def measure_value(self):
    # Reads pitch, raw, yaw and return tuple (x, y, z)
    sense = SenseHat()
    accel_value = sense.get_accelerometer_raw()
    x = accel_value.get('x')
    y = accel_value.get('y')
    z = accel_value.get('z')
    accel =(x, y, z)
    return accel

  def check_deviance(self, new_value: tuple) -> bool:
    """
    The function first compare the difference of each direction to find deviance
    Next it checks the deviance of the vector as a whole
    For now if the difference is over 25% of the average, then it is a deviant
    """
    deviance = False
    try:
      past_value = self.con.history[-5:]
      past_value_average = 0
      vector_average = 0

      for i in range(3):
        for t in range(5):
          past_value_average += past_value[t][i]
        if abs((new_value[i]-past_value_average / 5)/(past_value_average / 5)) > 0.5:
          deviance = True
        past_value_average = 0

      for a in range(5):
        vector_average += sum(map(lambda x:x**2, past_value[a]))
      vector_average = vector_average / 5
      if abs(sum(map(lambda x: x**2, new_value))-vector_average)/vector_average > 0.5:
        deviance = True

      return deviance
    except:
      return deviance

      

    
