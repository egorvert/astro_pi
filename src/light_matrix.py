# Egor and Stepan
from sense_hat import SenseHat
from time import sleep

class MatrixController():
  """Controller for methods and data related to the light matrix

  :param con: Reference to main controller
  :type con: main.Controller
  """
  def __init__(self, con):
    self.con = con

  def greeting(self):
    sense = SenseHat()

    sense.set_rotation(270)

    X = [255, 0, 0]  # Red
    O = [0, 0, 0]  # Black

    greeting_msg = "Hello world!"

    greeting_icon = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, X, O, O, O, O, X, O,
    X, O, X, O, O, X, O, X,
    O, O, O, O, O, O, O, O,
    O, X, O, O, O, O, X, O,
    O, O, X, X, X, X, O, O,
    O, O, O, O, O, O, O, O
    ]

    sense.show_message(greeting_msg, back_colour=O, text_colour=blue)
    sleep(1)
    sense.set_pixels(greeting_icon)

  def update(self, cam_changed: bool, acc_changed: bool, gyro_changed: bool):
    pass
