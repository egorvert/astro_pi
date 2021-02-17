from time import sleep


class MatrixController():
  """Controller for methods and data related to the light matrix

  :param con: Reference to main controller
  :type con: main.Controller
  """


  idleFM = [
    ["idle_fm_0.png",2500],
    ["idle_fm_1.png",150],
    ["idle_fm_2.png",1000],
    ["idle_fm_3.png",100],
    ["idle_fm_4.png", 1000],
    ["idle_fm_5.png",100]
    ]

  cameraReactionFM = [
    ["surprised_fm_0.png",1000],
    ["surprised_fm_1.png",150],
    ["surprised_fm_2.png",500],
    ["surprised_fm_3.png",150],
    ["surprised_fm_4.png",1000],
    ["surprised_fm_5.png",150],
    ["surprised_fm_6.png",1000]
    ]

  accelFM = [
    "accelerometer-frame-1.png",
    "accelerometer-frame-2.png"
    ]

  gyroFM = [
    "gyroscope-frame-1.png",
    "gyroscope-frame-2.png",
    "gyroscope-frame-3.png",
    "gyroscope-frame-4.png",
    "gyroscope-frame-5.png",
    "gyroscope-frame-6.png"
    ]
  
  
  
  def __init__(self, con):
    self.con = con
    self.sense = con.sense

    self.frame_queue = []

  def greeting(self):
    self.sense.set_rotation(270)

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
    ]  # yapf: disable

    self.sense.show_message(greeting_msg, back_colour=O, text_colour=blue)
    sleep(1)
    self.sense.set_pixels(greeting_icon)

  def update(self):
    if len(self.frame_queue) == 0:
      return
    self.sense.load_image(self.frame_queue.pop(0))

  def start_sequence(self, cam_changed: bool, acc_changed: bool, gyro_changed: bool):
    pass
