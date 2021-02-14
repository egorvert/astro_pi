<<<<<<< HEAD
from sense_hat import SenseHat
gyroList = [{'pitch': 76.2714433283, 'roll': 237.873941872, 'yaw': 71.2012831036}, {'pitch': 76.2714433283, 'roll': 237.873941872, 'yaw': 71.2012831036}, {'pitch': 76.2714433283, 'roll': 237.873941872, 'yaw': 71.2012831036}, {'pitch': 76.2714433283, 'roll': 237.873941872, 'yaw': 71.2012831036}]

def moving_window_average(x, n_neighbors=3):
  n = len(x)
  width = n_neighbors*2 + 1
  x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
  # To complete the function,
  return [sum(x[i:i+width] )*2/n  for i in range(n) ]

class GyroscopeController:
  """
    Controller for methods and data related to the gyroscope
    
    :param con: Reference to main controller
    :type con: main.Controller
  """
  sense = SenseHat()
  gyroList = []
  pitchList = []
  rollList = []
  yawList = []

while True:
  gyro_only = sense.get_gyroscope()
  gyroList.append(sense.get_gyroscope())
  for i in gyroList:
    pitchList.append([ i[name] for name in i.keys() if name == 'pitch' ])
    rollList.append([ i[name] for name in i.keys() if name == 'roll' ])
    yawList.append([ i[name] for name in i.keys() if name == 'yaw' ])




#   print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))



  # def __init__(self, con):
  #   self.con = con
=======
# Adam and Ben
from src.metric import MetricController


class GyroscopeController(MetricController):
  """Controller for methods and data related to the gyroscope
  
  :param con: Reference to main controller
  :type con: main.Controller
  """
  def __init__(self, con):
    super().__init__(1, 'gyroscope')
    self.con = con

  def measure_value(self):
    # Reads the value from the relevent module and returns it
    return 1
>>>>>>> fbccc2e13e5eac1734fd93a4ed3ff505639f7c85
