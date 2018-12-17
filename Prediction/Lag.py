
import pandas as pd
import matplotlib.pyplot as plt
import os
from LaggedReg import poly_reg

from Neuro_Net import nuero_net
from Data_Prep import data_prep as dp
import numpy as np
from Playground import playground

# lags the price by inputed amoung and peforms polynomial regression on the csv file in input
class lag(object):

    #does it all!
    #paramerter: lag - int - the desired lag between the word freq and the price
    def __init__(self,n):
        home_folder = os.path.dirname(os.path.realpath(__file__)).replace('\\','//')
        #Add the name of the input file here after input//
        src = home_folder + '//input//example_input.csv'

        #Add the name of the desired output file
        dest = home_folder + '//output//example_output.csv'

        raw = pd.read_csv(src)
        lag_array = []
        error_full = []
        #creats a data_prep objects. the methods in this class are used ajust the data
        for lag in range(30):
            lag = lag + 1

            # uncomment this and comment out other lines between ******
            #tot_data, tot_labels = playground.multiple_days(raw,lag)

            #code used to determine lag for a particular day
            #******************************************************
            data_prep = dp(raw)

            #lags the features by the inputed value
            data_prep.set_lag(lag)

            #aquire the data seperated
            tot_labels = data_prep.get_price()
            tot_data = data_prep.get_freq()
            #********************************************************

            column_names = tot_data.columns

            #inputs the data into the Neuro Net 10 times in order to find an average error

            errors = []

            for index in range(10):
                results = nuero_net(tot_data, tot_labels, column_names)
                print(results.get_error())
                errors.append(results.get_error())
            lag_array.append(lag)
            error_full.append(sum(errors)/float(len(errors)))
            print(lag)
            df = pd.DataFrame(data = [lag_array,error_full],index=['lag','error'])
            df.to_csv(dest)

