# Egor and Stepan
#TODO: make a program that recognises deviations in light intensity between 2 captures
import datetime
from time import sleep
import numpy as np
from picamera import PiCamera

from src.metric import MetricController


class CameraController(MetricController):  #, picamera.array.PiMotionAnalysis):
  """Controller for methods and data related to the light sensor/camera.
    
  :param con: Reference to main controller
  :type con: main.Controller
  """
  def __init__(self, con):
    super().__init__(0.1, 'camera')
    self.con = con
    self.sense = con.sense
    self.camera = PiCamera()
  def capture(self): #this needs to be done for example every 5 seconds
    i = 1 #this should be put in the main loop
    output1 = np.empty((480, 640, 3), dtype=np.uint8) #2 different arrays to capture 2 frames in so that they can be compared
    output2= np.empty((480, 640, 3), dtype=np.uint8) #this sould stay out of the main loop so that they are only made once
    camera.capture_effects = (128.128)
    camera.resolution = (640,480)
    if i % 2 != 0:
      camera.capture(output1, 'rgb')
    else:
      camera.capture(output2,'rgb')
    
    if i % 2 == 0:
      differences = np.subtract(output2,output1)
      print(differences)
    elif i % 2 != 0 and i != 1:
        differences = np.subtract(output1, output2)
    i+=1
    sleep(5) #captures 2 frames 5 seconds apart
   
        
    
