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

## Documentation Development
The code for this project is documented using [Sphynx](https://www.sphinx-doc.org/). This autogenerates documentation for the project by collating the docstrings of classes and functions in the code and formatting it into a dynamic web page. This can be found in the `docs/` folder.

To rebuild the documentation run the following command.
```
.\docs\make.bat html
```
The home page of the documentation is `docs/_build/html/index.html`.
