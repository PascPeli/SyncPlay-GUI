# [SyncPlay GUI](https://github.com/PascPeli/SyncPlay-GUI)

This is a Graphical User Interface(GUI) for [SyncPlay](https://syncplay.pl/).

<img src=https://raw.githubusercontent.com/PascPeli/SyncPlay-GUI/master/icons/image.png alt="Drawing" style="width: 1000px;"/>

The GUI offers almost the same experience as the default GUI provided by the installation of SyncPlay. I created this because syncplay uses PySide on their solution which has to be installed. This Solution is based on PyQt5. The executable found in this repository ("dist" folder) works without the need for installation.

You can create an anaconda environment by running

`conda env create -f environment.yml`

In case you make changes and want to recreate the executable you can run:

`pyinstaller -F -n syncplayGUI --icon=icons/syncplay.ico --noconsole MainWindow.py`
