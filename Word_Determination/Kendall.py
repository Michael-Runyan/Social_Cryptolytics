import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

class Kendall(object):


    #Performing Kendall Tau correlations
    #Parameters:    df-Data Frame
    #    columns of data frame should be as follows
    #    time   word1   word2   word... mean
    #               absval- Boolean - true if results should be returned as absolute values
    def __init__(self,df,absval):
        corr = []
        word = []
        self.Ken_Tau = word, corr
        data = df
        self.working_data = data

        for column in data.columns[1:len(df.columns)- 2]:
            temp = data[[column,'mean']].copy()
            Ken = temp.corr(method='kendall')
            try:
                if absval:
                    self.Ken_Tau[1].append(abs(Ken.iat[0, 1]))
                else:
                    self.Ken_Tau[1].append(Ken.iat[0,1])
                self.Ken_Tau[0].append(column)
            except IndexError:
                continue
        #print(Ken_Tau[1])


        self.sorted_words = [x for _,x in sorted(zip(self.Ken_Tau[1],self.Ken_Tau[0]))]
        self.sorted_corr = sorted(self.Ken_Tau[1])
    #returns a data frame of the calculated values
    def get_corr(self):
        return pd.DataFrame(data=self.sorted_corr, index=self.sorted_words, columns=["Coefficient"])
    def graph_results(self):
        plt.barh(self.sorted_words,self.sorted_corr, align='center', alpha=0.5)
        plt.ylabel('Correlation Coefficient')
        plt.title('Kendalls Tau Coefficient of Reddit Word Count')

        plt.show()
        return plt
    #knocks out any columns that are not rated as high as val_to_keep
    #parameter: int val_to_keep, number between 0 and 1
    def shrink_columns(self,val_to_keep):
        ken_val = self.sort()

        kept_var = []
        for i in range(len(ken_val[0])):
       #     print(ken_val[1][i])
            if ken_val[1][i] >= val_to_keep:
                kept_var.append(ken_val[0][i])

        # creats a data frame from selcected feautures
        self.shrunk_data = pd.DataFrame()

        column_names = []
        tot_data = []
        for feature in kept_var:
            temp_df = self.working_data[feature]
            self.shrunk_data = self.shrunk_data.append(temp_df)
            column_names.append(feature)
        self.column_names = column_names

        #converts to numpy array to transpose and then converts back to dataframe
        self.shrunk_data = self.shrunk_data.as_matrix()
        self.shrunk_data = self.shrunk_data.transpose()

        self.shrunk_data = pd.DataFrame(self.shrunk_data,columns=column_names)
    def sort(self):
        return self.sorted_words,self.sorted_corr
    def get_results(self):
        return self.shrunk_data
    def get_column_names(self):
        return self.column_names
#works
 #   Ken_Tau = data.corr(method='kendall')
#print(accept.corr(method='kendall'))


#accept_count_and_price = data['accept'],data['mean']
#data.corr(method='kendall')
#print(accept_count_and_price)