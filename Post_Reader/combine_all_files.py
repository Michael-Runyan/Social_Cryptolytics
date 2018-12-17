import pandas as pd
import os

home_folder = (os.path.dirname(os.path.realpath(__file__))).replace('\\','//')
start = pd.read_csv('starter_template//starter_template.csv')
end = start
#second_file = pd.read_csv('sample_2.csv')
time = start['Unnamed: 0']

for csv_file in os.listdir(home_folder):

    if csv_file.endswith(".csv"):
        temp = pd.read_csv(csv_file)
        end = end.add(temp,fill_value=0)
        end['Unnamed: 0'] = end['Unnamed: 0'] - time


end.to_csv('combined_elements.csv')