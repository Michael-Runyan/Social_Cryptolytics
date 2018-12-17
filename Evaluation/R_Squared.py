import pandas as pd
import os
import sklearn.metrics as sk

home_folder = os.path.dirname(os.path.realpath(__file__)).replace('\\', '//')
src = home_folder + '//input//days_90_pred_val.csv'
dest = home_folder + '//output//line_reg_coef_avg.csv'


raw = pd.read_csv(src)

pred_val = raw['prediction'].copy()
real_val = raw['label'].copy()

print(sk.r2_score(real_val,pred_val))


