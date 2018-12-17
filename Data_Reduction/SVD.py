import pandas as pd
import numpy as np

class svd(object):

    #parameter:
    #   data- panda Dataframe
    #   columns - list - list of the column names of the data frame
    def __init__(self,data,columns):
        self.columns = columns
        self.org_data = data
    def perform_svd(self,to_keep):

        c_names = list(self.org_data)

        U, sigma, V = np.linalg.svd(self.org_data)

        # V is an nxn array, columns have kept their original alignment
        # columns that are similar will have similar values
        # Column 1 and 4 are close while 2 and 3 are similar
        V_df = pd.DataFrame(V, columns=c_names)
        # print(V_df)

        # calculates the percentage that each post accounts for the variance
        sum = np.sum(sigma)
        per_variance = []
        for component in sigma:
            temp = component / sum
            per_variance.append(temp)
        per = 0
        num_col = to_keep
        # calculates number of variables it takes to reperestent x of the array
#        while per < .95:
#            per = per + per_variance[num_col]
#            num_col = num_col + 1

        col_list = list(V_df)
        differences = []
        sub_names = []
        sub_one = []
        sub_two = []
        # determines which varibles are most related, smaller the number the more similar
        for col in range(len(col_list)):
            sub = col + 1
            while sub < len(col_list):
                differences.append(((V_df[col_list[col]] - V_df[col_list[sub]]).abs()).sum())
                sub_names.append(str(col_list[col]) + ' - ' + str(col_list[sub]))
                sub_one.append(str(col_list[col]))
                sub_two.append(str(col_list[sub]))
                sub = sub + 1

        # organizes the data into one data frame and sorts them by varience
        sub_one = pd.DataFrame(sub_one, columns=['1st post'])
        sub_two = pd.DataFrame(sub_two, columns=['2nd post'])
        differences = pd.DataFrame(differences, columns=['compared'])
        col_var = pd.concat([sub_one, sub_two, differences], axis=1, join_axes=[sub_one.index])
        col_var = col_var.sort_values('compared', ascending=True)
        print(col_var)

        set_index = np.arange(0, col_var.shape[0])
        col_var.set_index(set_index, inplace=True)
        # determines which columns to include, if one column was going to be used twice this picks the second column it was compared to
        final_col = []
        indexer = 0
        loop_iter = num_col
        #for indexer in range(num_col):
        while indexer < loop_iter:
            add_to = col_var.loc[indexer, '1st post']
            if final_col.__contains__(add_to):
                add_to = col_var.loc[indexer, '2nd post']
                if final_col.__contains__(add_to):
                    indexer = indexer + 1
                    loop_iter = loop_iter + 1
                    continue
            final_col.append(add_to)
            indexer = indexer +1
        self.final_col = final_col
        print(self.final_col)

    def get_knocked_data(self):
        self.working_data = pd.DataFrame(columns=self.final_col)
        for feature in self.final_col:
            self.working_data[feature] = self.org_data[feature]
        return self.working_data

    def get_columns(self):
        return self.final_col

