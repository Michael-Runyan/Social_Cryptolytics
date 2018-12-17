#classed used to find the number of elements in the series which predict the distribution

import os
import pandas as pd
from Graph_Tools import graph_tools as gt

home_folder = os.path.dirname(os.path.realpath(__file__)).replace('\\', '//')
input = home_folder + '//input//'
output = home_folder + '//output//'

src = input+  'combined_elements.csv'

df = pd.read_csv(src)

time,freq = gt.sum_rows(df)

#quick save of the freq
# result = pd.concat([time, freq], axis=1)
# result.columns = ['time','Freq']
# result.to_csv(output + 'comb_freq.csv')

# freq = df['Freq'].copy()
# time = df['time'].copy()
#
tot = freq.sum()

num_l = []
ratio_l = []
max_per_l = []
num = 2000
for index in range(1):
    num = num
    per = []
    where = []
    for index in range(len(freq)-num):
         per.append(sum(freq[index:index + num])/tot)
         where.append(index)


    max_per = max(per)
    ratio = max_per/(num/len(freq))
    loc = where[per.index(max_per)]

    print('num: ' + str(num))
    print('ratio: ' + str(ratio))
    print('per: ' + str(max_per))
    print('location: ' + str(loc))
    print('end loc unix: ' + str(time[loc+num]))
    print('end loc data: ' + gt.unix_to_date(time[loc + num],'%m  /  %d  /  %Y'))
