# Astro Pi Competition Entry
An entry piece for the [**Astro Pi _Mission Space Lab_**](https://astro-pi.org/mission-space-lab/) competition written in Python3. All code and functionality was developed by team _, consisting of
Adam Heal, 
[Gregor Maclaine](https://github.com/gregormaclaine), 
[Stepan Mikoyan](https://github.com/stepstoglory), 
[Ben Nason](https://github.com/NasonBen), 
[Egor Vert](https://github.com/Melon-Bowl), and 
[Yichen Xu](https://github.com/AXuyc).

For a more detailed reference on the code itself see the [documentation](https://melon-bowl.github.io/astro_pi/build/html/index.html).

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
The code for this project is documented using [Sphinx](https://www.sphinx-doc.org/). This autogenerates documentation for the project by collating the docstrings of classes and functions in the code and formatting it into a dynamic web page. This can be found in the `docs/` folder.

To rebuild the documentation run the following command.
```
.\docs\make.bat html
```
*Note: Sometimes Sphinx does not always update pages not directly changed during editing. So sometimes it is necessary to delete teh `docs/build` folder and rebuild it using the command above.*

The home page of the documentation is `docs/index.html`.
