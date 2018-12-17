import numpy as np
import pandas as pd

#Provides methods to assist in performing regression
class work_help(object):


    #divides the data in a traing set and a testing sit
    #paramter:  tot_data -Dataframe - feautures
    #           tot_labels -Dataframe - Dependant variables
    #           column_names - Series - name of each feauture
    #returns: An array with [train_data,train_labels,test_data,test_labels]
    @staticmethod
    def split_data(tot_data, tot_labels, column_names):
        tot_labels = tot_labels.as_matrix()
        tot_data = tot_data.as_matrix()

        # Shuffle the training set and test set
        order = np.argsort(np.random.random(tot_labels.shape))
        # parameters shuffled
        tot_data = tot_data[order]
        # price shuffled
        tot_labels = tot_labels[order]

        row, col = tot_data.shape

        train = int(row * .75)

        train_data = tot_data[:train]
        train_labels = tot_labels[:train]

        test_data = tot_data[train:]
        test_labels = tot_labels[train:]

        #   print('Train data: ' + str(train_data.shape))
        #  print('Test data: ' + str(test_data.shape))

        # creates data frame
        df = pd.DataFrame(train_data, columns=column_names)

        # adds the column names i think
        df.head()
        return [df,train_labels,test_data,test_labels]
    @staticmethod
    def mean_abs_error(pred,labels):
        error_a = []
        for index in range(len(labels)):
            error_a.append(abs(pred[index]-labels[index]))

        mean_e = sum(error_a)/len(error_a)
        return mean_e