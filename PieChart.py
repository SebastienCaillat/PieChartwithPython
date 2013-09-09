""" Small program to create pie graphs with or without hatching
Please note that if hatching selected, values will no apear inside the pie
one option is to add values in the labels i.e. 'toto \n 10 %'
Usage: data to be filled in the program then run to generate figure
    Argument after program name will change figure filename
    nofile will avoid saving figure to file
Modules needed: numpy, matpotlib, pylab... see error message and install missing module
unedr windows, Unofficial Windows Binaries for Python Extension Packages
can help: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pandas
tested with Python 3.3
First version S. Caillat 9/9/2013
"""
import matplotlib.pyplot as plt
from pylab import *
import os,sys
def help():
    scriptname = os.path.basename(sys.argv[0])
    print("Usage:")
    print(scriptname+' with no argument: print & save data to file')
    print(scriptname+' <file_name>: chose figure.png file name')
    print(scriptname+' <nofile>: just display, no data file saved')
    print('See setting in file '+scriptname+' for other options') 
    sys.exit()
# ---------------- Settings -----------------------------------------
filename= "Pie-figure"              # default file name
savedata=True                       # save figure (default value True)
shadow=True                         # shadow True or False
hatch=True                          # hatching or not (True or False)
startangle = 180                    # try 0, 90 or 180

# ---------------- Insert data here: -------------------------------
labels = 'Carbone\n54,2 %','Hydrogène\n 6,22 %','Oxygène\n39,0 %',\
         'Azote\n 0,39 %',' '
sizes = [54.2,6.22,39.0,0.39,0.19]
explode = (0.1,0,0,0,0)      # explode is optional
colors = ['#E41A1C','#377EB8', '#4DAF4A','#984EA3','#FF7F00','#FFFF33'
          ,'#A65628','#F781BF','#999999']
        #  'blue','green','red','cyan','magenta']
hatching = ["//","||",'\\\\',"--",'+']
# hatching accepted : /,\,|,-,+,x,o,O,.,*  repeat symbol for higher density
# ---------------- end of settings ----------------------------------
if len(sys.argv) > 1:
    filename=sys.argv[1]  # Project name to add to filename
    if filename =='help' or filename =='?': help()
    if filename =='nofile': savedata = False

if hatch == True :
    fig, ax = plt.subplots()
    wedges, texts = ax.pie(sizes,colors=colors,labels=labels,
                       explode=explode, shadow=shadow, startangle=startangle)
    for j, patch in enumerate(wedges): patch.set_hatch(hatching[j])
    gca().set_aspect('equal') # square the figure
    if savedata == True : fig.savefig(filename+".png")
else :
    plt.pie(sizes,colors=colors,labels=labels,
            explode=explode, shadow=shadow, startangle=startangle,
            # autopct="%1.1f %%" # remove comment for value display
            )
    gca().set_aspect('equal') # square the figure
    if savedata == True : savefig(filename+'.png') # pdf or svg also possible
show()

