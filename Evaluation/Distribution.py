import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from Graph_Tools import graph_tools as gt
sns.set()

home_folder = os.path.dirname(os.path.realpath(__file__)).replace('\\', '//')
input = home_folder + '//input//'
output = home_folder + '//output//'

src = input+  'comb_freq.csv'

df = pd.read_csv(src)

freq = df['Freq'].copy()
time = df['time'].copy()
tot = freq.sum()


bins = []
start = 12
year = []
count = 0
mid_count = []
num_bins = 25
interval = 80

for index in range(num_bins):
    bins.append((freq[start:start+interval].sum())/tot)
    #takes the unix time and spits out the date
    year.append(gt.unix_to_date(time[start + (interval/2)],'%Y'))
    mid_count.append(gt.unix_to_date(time[start + (interval/2)],'%m/%Y'))
    start = start + interval
    count = count + 1


num = 14
per = []
where = []
for index in range(len(bins)-num):
    per.append(sum(bins[index:index + num]))
    #where.append()

print(per)
print(max(per))
x_tick = []
for label in np.arange(0,len(mid_count),5):
    x_tick.append(mid_count[label])

#adds a label to the very end
x_tick.append(mid_count[len(mid_count)-1])

plt.bar(mid_count,bins)
plt.xticks(x_tick)

plt.xlabel('Time')
plt.ylabel('Percentage of Total Word Count (%)')
plt.title('Word Count Distribution')
plt.show()

