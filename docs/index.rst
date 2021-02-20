Wellington College Astro Pi Docs
================================
The code for this project is split into separate files that manage a certain aspect of the program.
These components are connected together via references in a main `Controller` class, which manages the top level structure and operation of the program.

On submition, the code should be compiled to one file; the code itself should not have to be modified.

`See the code for the project here <https://github.com/Melon-Bowl/astro_pi>`_

.. toctree::
	:maxdepth: 2
	:caption: Main Classes:
	
	pages/metric
	pages/light_matrix
	pages/output
	pages/test_modules

.. toctree::
	:maxdepth: 2
	:caption: Components:
	
	pages/accelerometer
	pages/camera
	pages/gyroscope

.. toctree::
	:maxdepth: 2
	:caption: Other:
	
	pages/frames

Main Controller
***************

.. module:: main

.. autoclass:: Controller
	:members: