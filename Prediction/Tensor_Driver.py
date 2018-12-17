import pandas as pd
import matplotlib.pyplot as plt
import os
from LaggedReg import poly_reg

from Neuro_Net import nuero_net
from Data_Prep import data_prep as dp

#this file runs the keras model
lag = 0
home_folder = os.path.dirname(os.path.realpath(__file__)).replace('\\', '//')

#add the file which will be used as input
src = home_folder + '//input//example_input.csv'

#Add the destination
dest = home_folder + '//output//example_out.csv'

raw = pd.read_csv(src)
# creats a data_prep objects. the methods in this class are used ajust the data
data_prep = dp(raw)

# lags the features by the inputed value
data_prep.set_lag(12)

#Or comment out below between ********* and use this to set the number of days prior to use
#tot_data, tot_labels = playground.multiple_days(raw,lag)

#*************************
# aquire the data seperated
tot_labels = data_prep.get_price()
freq_data = data_prep.get_freq()
tot_data = freq_data
#***************************
column_names = tot_data.columns

# inputs the data into the Neuro Net 10 times in order to find an average error

results = nuero_net(tot_data, tot_labels, column_names)
print(results.get_error())
