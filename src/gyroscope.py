from sense_hat import SenseHat

gyroOrent ={
  'pitch': 76.2714433283,
  'roll': 237.873941872,
  'yaw': 71.2012831036
} # test data


# def moving_window_average(x, n_neighbors=3):
#   n = len(x)
#   width = n_neighbors * 2 + 1
#   x = [x[0]] * n_neighbors + x + [x[-1]] * n_neighbors
#   return [sum(x[i:i + width]) * 2 / n for i in range(n)]


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
    gyroOrent = sense.get_gyroscope()
    pitchList.append([gyroOrent[i] for i in gyroOrent if i == 'pitch']) 
    rollList.append([gyroOrent[i] for i in gyroOrent if i == 'roll']) 
    yawList.append([gyroOrent[i] for i in gyroOrent if i == 'yaw'])

# def __init__(self, con):
#   self.con = con
