from time import sleep


class FrameSequence:
  # yapf: disable
  idle = [
    ['face/smile.png', 2500],
    ['face/flat.png',  150 ],
    ['face/right.png', 1000],
    ['face/flat.png',  100 ],
    ['face/left.png',  1000],
    ['face/flat.png',  100 ]
  ]

  camera = [
    ['face/smile.png',     1000],
    ['face/flat.png',      150 ],
    ['face/openbig.png',   500 ],
    ['face/opensmall.png', 150 ],
    ['face/openbig.png',   1000],
    ['face/opensmall.png', 150 ],
    ['face/openbig.png',   1000]
  ]

  accel = [
    ['rocket/1.png', 250],
    ['rocket/2.png', 250]
  ] * 6

  gyro = [
    ['teetotum/1.png', 250],
    ['teetotum/2.png', 250],
    ['teetotum/3.png', 250],
    ['teetotum/4.png', 250],
    ['teetotum/5.png', 250],
    ['teetotum/6.png', 250]
  ] * 3
  # yapf: enable


class MatrixController:
  """Controller for methods and data related to the light matrix

  :param con: Reference to main controller
  :type con: main.Controller
  """
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
