Dummy Modules
=========================

The file ``src/test_modules.py`` contains classes that should only be used in testing.
The modules **SenseHat** and **PiCamera** are built to be run on a RaspberryPi with the correct
hardware attached. However, we wanted to be able to run and test the program on a laptop during
the development process. Therefore this file supplies dummy methods and functions to let the
main processes work as if these devices were connected by returning random data in the correct format.

.. module:: src.test_modules

.. autoclass:: SenseHat
	:members:

.. autoclass:: PiCamera
	:members:
