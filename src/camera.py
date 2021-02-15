# Egor and Stepan
import datetime
from time import sleep
import numpy as np
from picamera import PiCamera

from src.metric import MetricController


class CameraController(MetricController, picamera.array.PiMotionAnalysis):
  """Controller for methods and data related to the light sensor/camera.
    
  :param con: Reference to main controller
  :type con: main.Controller
  """
  def __init__(self, con):
    super().__init__(0.1, 'camera')
    self.con = con
    self.sense = con.sense

  def analyze(self, a):
    #functiont that determines whether there is motion by looking at vectors with magnitudes larger than 60
    a = np.sqrt(
      np.square(a['x'].astype(np.float)) + np.square(a['y'].astype(np.float))
    ).clip(0, 255).astype(np.uint8)
    if (a > 60).sum() > 10:
      print("Motion detected! at %s" % (datetime.datetime.now()))
      #change to light matrix output and save a true or false boolean to the main data file with a datetime

  # Reads the value from the relevant module and returns it
  def measure_value(self) -> float:
    pass


while True:  #Change this so that it doesnt get stuck
  with picamera.PiCamera() as camera:
    with CameraController(camera) as data_out:
      camera.resolution = (640, 480)
      camera.start_recording(
        '/dev/null', format='h264', motion_output=data_out
      )  #records for 60 s V
      camera.wait_recording(60)
      camera.stop_recording()
