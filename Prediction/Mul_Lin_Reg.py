import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
from Work_Help import work_help as wh
from Data_Prep import data_prep

home_folder = os.path.dirname(os.path.realpath(__file__)).replace('\\', '//')
src = home_folder + '//input//svd_freq.csv'
dest = home_folder + '//output//line_reg_coef_avg.csv'

df = pd.read_csv(src)

wk_data = data_prep(df)
wk_data.set_lag(12)
features =(wk_data.get_freq())
labels =(wk_data.get_price())


co_tot = pd.DataFrame(index = features.columns)
co_tot = co_tot.fillna(0)

avg_r = []
avg_error = []
indexer = 100
for index in range(indexer):
    train_data,train_labels,test_data,test_labels= wh.split_data(features,labels,features.columns)

    model = sm.OLS(train_labels,train_data).fit()
    predictions = model.predict(test_data)


    avg_r.append(model.rsquared)
    mean_error = wh.mean_abs_error(predictions,test_labels)
    avg_error.append(mean_error)
    co_tot = pd.concat([co_tot,model.params],axis=1)


co = (co_tot.sum(axis=1).divide(indexer))
avg_r = (sum(avg_error)/len(avg_error))
avg_error = (sum(avg_error)/len(avg_error))

print(avg_error)
print(avg_r)
print(co)
lin_coef = pd.DataFrame(data = co,columns = ['coefficients'])
lin_coef.to_csv(dest)
#print(model.summary())