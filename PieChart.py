#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Small program to create pie graphs with or without hatching

Please note that if hatching selected, values will no apear inside the pie
one option is to add values in the labels i.e. 'toto \n 10 %'
Usage : date to be filled in the program then run to generate figure
    Argument after program name will change figure filename
    nofile will avoid saving figure to file
Last update S. Caillat 22/03/2014"""
import matplotlib.pyplot as plt
from pylab import *
import os,sys
def help():
    scriptname = os.path.basename(sys.argv[0])
    print("Usage:")
    print(scriptname+' <file_name>: chose figure.png file name')
    print(scriptname+' <nofile>: just display, no data file saved')
    print('See setting in file '+scriptname+' for other options') 
    sys.exit()
# ---------------- Settings -----------------------------------------
filename = "Pie-figure"             # default file name
savedata = True                     # True/False: save figure to file
shadow = True                       # True or False: shadow
hatch = True                        # True or False: hatching
startangle = 180                    # for example 0, 90 or 180
labeldistance = 1.15                # label distance from pie
# ---------------- Insert data here: -------------------------------
labels = 'Carbone\n54,2 %','Hydrogène\n 6,22 %','Oxygène\n39,0 %',\
         'Azote\n 0,39 %',' '
sizes = 54.2,6.22,39.0,0.39,0.19
explode = 0.1,0,0,0,0      # explode is optional
colors = '#E41A1C','#377EB8', '#4DAF4A','#984EA3','#FF7F00','#FFFF33'\
        ,'#A65628','#F781BF','#999999'
# colors = '#8a56e2','#cf56e2','#e256ae','#e25668','#e28956',
# '#e2cf56','#aee256','#68e256','#56e289','#56e2cf','#56aee2','#5668e2'
# 'blue','green','red','cyan','magenta'
# '#FF0000','#FF7400','#009999','#00CC00'
hatching = "//","||",'\\\\',"--",'+'
# hatching accepted : /,\,|,-,+,x,o,O,.,*  repeat symbol for higher density
# ---------------- end of settings ----------------------------------
if len(sys.argv) > 1:
    filename=sys.argv[1]  # Project name to add to filename
    if filename =='help' or filename =='?': help()
    if filename =='nofile': savedata = False

if hatch == True :
    fig, ax = plt.subplots()
    wedges, texts = ax.pie(sizes,colors=colors,labels=labels,
                    explode=explode, shadow=shadow, startangle=startangle,
                    labeldistance=labeldistance)
    for j, patch in enumerate(wedges): patch.set_hatch(hatching[j])
    gca().set_aspect('equal') # square the figure
    if savedata == True : fig.savefig(filename+".png")
else :
    plt.pie(sizes,colors=colors,labels=labels,
            explode=explode, shadow=shadow, startangle=startangle,
            labeldistance=labeldistance,
            # autopct="%1.1f %%" # remove comment for value display
            )
    gca().set_aspect('equal') # square the figure
    if savedata == True : savefig(filename+'.png') # pdf or svg also possible
show()
