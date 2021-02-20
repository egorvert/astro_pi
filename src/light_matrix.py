class FrameSequence:
  """A namespace for frame sequences"""
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
    ['rocket/2.png', 250],
    ['rocket/3.png', 250],
    ['rocket/4.png', 250]
  ] * 3

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
  """Controller for the LED light matrix and what to show on it.

  :param con: Reference to main controller
  :type con: main.Controller
  """
  def __init__(self, con):
    self.con = con
    self.sense = con.sense

    self.frame_queue = []
    self.frame_time_left = 0.0
    self.timeperiod = 50.0

  def set_framerate(self, framerate: int):
    """Sets the framerate of the main loop so that the controller
    can calculate how long to show each frame.

    :param framerate: The number ``update()`` calls per second
    :type framerate: int
    """
    self.timeperiod = 1000 / framerate

  def load_image(self, image: str):
    """Shows a 8x8 image on the LED matrix

    :param image: The image filename
    :type image: str
    """
    try:
      self.sense.load_image(image)
    except Exception as err:
      self.con.output.log(f'Could not show frame "{image}"', err)

  def update(self):
    """Handles the iteration and dynamics of the frame sequences.
    Should be called once per main loop cycle after the framerate has been
    set in the ``set_framerate()`` method.\n
    It works by either keeping the current frame, or moving onto the next frame in
    the sequence. If no more frames are stated, it defaults to showing ``FrameSequence.idle``.
    """
    if self.frame_time_left <= 0:
      if len(self.frame_queue) == 0:
        self.frame_queue += FrameSequence.idle
      frame = self.frame_queue.pop(0)
      self.load_image(frame[0])
      self.frame_time_left = frame[1]
    else:
      self.frame_time_left -= self.timeperiod

  def start_sequence(self, cam_changed: bool, acc_changed: bool, gyro_changed: bool):
    """Handles changing the current frame sequence in response to a possible deviance
    found after measuring the hardware components.

    :param cam_changed: Whether the camera value deviated
    :type cam_changed: bool
    :param acc_changed: Whether the accelerometer value deviated
    :type acc_changed: bool
    :param gyro_changed: Whether the gyroscope value deviated
    :type gyro_changed: bool
    """
    if cam_changed or acc_changed or gyro_changed:
      if cam_changed:
        self.con.output.log('Matrix: Showing camera animation')
        sequence = FrameSequence.camera
      elif gyro_changed:
        self.con.output.log('Matrix: Showing gyroscope animation')
        sequence = FrameSequence.gyro
      else:
        self.con.output.log('Matrix: Showing accelerator animation')
        sequence = FrameSequence.accel

      self.frame_queue.clear()
      self.frame_time_left = 0
      self.frame_queue += sequence
