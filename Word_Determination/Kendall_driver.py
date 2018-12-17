from Kendall import Kendall
import pandas as pd
import numpy as np
from Data_Prep import data_prep as dp

file = 'all_clean_2.0.csv'
save_file = 'C://Users//Michael//Documents//Current_Classes//D_Study//LAST_MILE//output//'

org_data = pd.read_csv(file,dtype={'user_id': float})

data_prep = dp(org_data)


data_prep.lag_features(0)
working_data_1 = data_prep.get_data()

ken = Kendall(working_data_1,absval=False)
(ken.get_corr()).to_csv(save_file + 'all_coeff.csv')
