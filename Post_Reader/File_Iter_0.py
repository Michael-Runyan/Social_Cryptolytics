
import os
import pandas as pd
import numpy as np
from Word_Search import word_search

parent = 0
home_folder = os.path.dirname(os.path.realpath(__file__))
folder = os.path.join(home_folder,'input//posts//parent_' + str(parent)).replace('\\','//')
word_file = os.path.join(home_folder,'input\words\AFINN_shrunk.txt').replace('\\','//')
time_file = os.path.join(home_folder,r'input\time\time.csv').replace('\\','//')
save_file = os.path.join(home_folder,r'output\sample_13_out_' + str(parent)+ '.csv').replace('\\','//')

matrix = word_search(word_file,time_file)


#walks through 3 layers of files
for root, dirs, files in os.walk(folder):
    for name in files:
        filename = root.replace('\\','//') + '//' + name
        if filename.endswith(".csv") or filename.endswith(".py"):
            matrix.search(filename)
            continue
        else:
            continue
print('saving')
matrix.save(save_file)
