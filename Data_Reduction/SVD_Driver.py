import pandas as pd
from SVD import svd
import os

#finds current folder
home_folder = os.path.dirname(os.path.realpath(__file__)).replace('\\','//')
src = home_folder + '//input//all_clean_2.0.csv'
dest = home_folder + '//output//svd_reduced_all.csv'
#reads the csv file into a data fram
word_count = pd.read_csv(src)

#saves the time col from the data frame
time_col = word_count['time']

##################check file and see what I really need here
#removes the extra col at beginning and the time col, this leaves the dataframe ready to be analyzed
word_count = word_count.drop(columns = ['time','mean'])
print(word_count)
#Creates an object of the SVD class
working_data = svd(word_count,word_count.columns)

#performs SVD and determines which columns will reduce the columns the the 100 which show the most varience
working_data.perform_svd(100)

keep_col = working_data.get_columns()
#print(keep_col)

#this is just a sample for testing
#keep_col = ['WEEPING', 'WEEP', 'WARMTH', 'WANKER', 'WALKOUTS', 'WALKOUT', 'VIVACIOUS', 'VITRIOLIC', 'VITALITY']


reduced_df =  word_count[keep_col]
reduced_df = reduced_df.rename(index = time_col)
reduced_df.index.name = 'time'


reduced_df.to_csv(dest)