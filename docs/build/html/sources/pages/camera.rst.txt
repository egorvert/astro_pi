Camera
======

This controller measures values using the **PiCamera** module. However, during development methods using
this module could not be tested due to our team not having access to the testing RaspberryPi.
Therefore a disclaimer was added to the beginning of the file ``camera.py`` asking for this fact to
be taken into consideration. Of course with this inconvenience in consideration, all methods using it
were wrapped in exception handling to prevent any errors from distrupting the rest of the working program.

.. module:: src.camera

.. autoclass:: CameraController
	:members: