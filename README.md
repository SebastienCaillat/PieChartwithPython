PieChartwithPython
==================

##Simple pie chart creation with hatching

Small program in Python 3 to create pie graphs with or without hatching, file is saved in png (also pdf or svg).

Please note that if hatching selected, values will no apear inside the pie,
one option is to add values in the labels i.e. 'toto \n 10 %'

## Usage
* Data, color shoice, symbols are to be filled in the program then run `PieChart.py` to generate figure
* Argument after program name will change figure filename
* `PieChart.py nofile` will avoid saving figure to file
* Other optin are to be changed inside the program
* If needed, color shemes can be found here http://colorbrewer2.org/ thanks to Cynthia A. Brewer

## Modules needed
* Numpy, matpotlib (http://matplotlib.org/), pylab... see error message if any
* Under Windows if needed use the Unofficial Windows 
Binaries for Python Extension Packages by Christoph Gohlke:
http://www.lfd.uci.edu/~gohlke/pythonlibs/ 


Tested with Python 3.3
