import pandas as pd
import numpy as np

class data_prep(object):

    #Ajusts an inputed DataFrame
    #parameter: Panda Data Frame - should have a labeled time and mean column
    def __init__(self,org_data):
        self.org_data = org_data

    #shifts the price up by the lag amount
    #parameter: lag- Positive int
    def set_lag(self,lag):
        temp_mean = self.org_data.loc[:,'mean']
        self.working_data = self.org_data[:len(self.org_data.index) - lag].copy()
        self.working_data = self.working_data.drop('mean',1)
        temp_mean = temp_mean.shift(-lag)[:-lag]

        self.working_data = pd.concat([self.working_data, temp_mean], axis=1, join_axes=[self.working_data.index])
  #      self.working_data = self.org_data[:len(self.org_data.index) - lag].copy()
#        for index in self.working_data['mean'].index:
#
 #           self.working_data['mean'][index] = self.org_data['mean'][index + lag]
 #       self.shifted_price = self.working_data['mean']

        # cuts off end of df by lag amount

    def get_data(self):
        return self.working_data

    def get_shifted_price(self):
        return self.shifted_price
    def get_price(self):
        return self.working_data['mean']

    #returns just the freqencies of the words
    def get_freq(self):
        return self.working_data.drop(columns = ['time','mean'])

