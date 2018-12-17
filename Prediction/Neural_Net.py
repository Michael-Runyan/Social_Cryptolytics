from Net_Helper import PrintDot
import matplotlib.pyplot as plt
import numpy as np
from Net_Helper import net_helper
import pandas as pd
from tensorflow import keras
import pydot
import graphviz
import seaborn as sn
sn.set()

class nuero_net(object):
    def __init__(self,tot_data,tot_labels,column_names):
        tot_labels = tot_labels.as_matrix()
        tot_data = tot_data.as_matrix()

        # Shuffle the training set and test set
        order = np.argsort(np.random.random(tot_labels.shape))
        #parameters shuffled
        tot_data = tot_data[order]
        #price shuffled
        tot_labels = tot_labels[order]

        row,col = tot_data.shape

        train = int(row*.75)

        train_data = tot_data[:train]
        train_labels = tot_labels[:train]

        test_data = tot_data[train:]
        test_labels = tot_labels[train:]

 #   print('Train data: ' + str(train_data.shape))
  #  print('Test data: ' + str(test_data.shape))

        #creates data frame
        df = pd.DataFrame(train_data, columns=column_names)

        #adds the column names i think
        df.head()

        #normalizes the training data to be between -1 and 1
        mean = train_data.mean(axis=0)
        std = train_data.std(axis=0)
        train_data = (train_data - mean) / std
        test_data = (test_data - mean) / std

        #builds the model for the nuero net
        model = net_helper.build_model(train_data)


        EPOCHS = 500

        #add to call backs to view history in tensorboard
        # tb = keras.callbacks.TensorBoard(log_dir='./Graph',
        #                             write_graph=True,
        #                             write_images=True,
        #                             histogram_freq = 50,
        #                             write_grads = True,
        #
        #                                  )
        #allows the training to stop once model stops improving
        early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=20)
        history = model.fit(train_data, train_labels, epochs=EPOCHS,
                            validation_split=0.2, verbose=0,
                           callbacks=[early_stop]) #, PrintDot()])
        hist = pd.DataFrame(history.history)
        hist['epoch'] = history.epoch
        hist.tail()

        #creates predictions for the test data from the model and saves them
        #test_predictions = model.predict(test_data).flatten()
        #quick = pd.DataFrame([test_labels,test_predictions],index=['label','prediction'])
        #quick.to_csv('C://Users//Michael//Documents//Current_Classes//D_Study//data//prediction_error_2.csv')


        [loss, mae] = model.evaluate(test_data, test_labels, verbose=0)

        #print("Testing set Mean Abs Error: ${:7.2f}".format(mae))
        self.error = mae
    def get_error(self):
        return self.error

