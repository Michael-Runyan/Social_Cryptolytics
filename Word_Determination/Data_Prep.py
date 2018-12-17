

class data_prep(object):

    def __init__(self,org_data):
        self.org_data = org_data

    #shifts the price up by the lag amount
    #parameter: lag- Positive int
    def set_lag(self,lag):
        temp = self.org_data['mean'].shift(lag)
        self.shifted_price = temp[lag:]
        # cuts off end of df by lag amount
        self.working_data = self.org_data[:len(self.org_data.index) - lag]

    #just be aware that this shifts the high low, and sd too
    #shifts the features back by lag
    #parameter lag- negative integer
    def lag_features(self,lag):
        price = self.org_data['mean']
        self.working_data = self.org_data.shift(lag)
        self.working_data = self.working_data[:len(self.working_data)+lag]
        self.working_data['mean'] = price
    def get_data(self):
        return self.working_data

    def get_shifted_price(self):
        return self.shifted_price
    def get_price(self):
        return self.working_data['mean']

