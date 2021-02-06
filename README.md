# Astro Pi Competition
Code for the astro-pi competition written in Python3 by team underscore.

## Use
To run the program, you must first ensure that you have the correct dependencies installed. A list of these is stored in the file `requirements.txt` in the root directoy. To download these run the following command.
```
pip install -r requirements.txt
```
Then you can start the program simply by running the command below.
```
python main.py
```
*Note that this assumes that `python` and `pip` are already saved in PATH and correspond to the correct Python3 .exe files*

## Python Files
The code for this project is split into separate files that manage a certain aspect of the program.
These mini-modules are connected together via references in a main `Controller` class, which manages the top level structure and operation of the program.

On submition, the code should be compiled to one file; the code itself should not have to be modified.
