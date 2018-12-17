from tensorflow import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

class net_helper(object):

    #builds model with two densly connected hidden layers and continuous output
    @staticmethod
    def build_model(train_data):
        model = keras.Sequential([
            keras.layers.Dense(64, activation=tf.nn.relu,
                               input_shape=(train_data.shape[1],)),
            keras.layers.Dense(64, activation=tf.nn.relu),
            keras.layers.Dense(1)
        ])

        optimizer = tf.train.RMSPropOptimizer(0.001)

        model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=['mae'])
        return model
    @staticmethod
    def plot_history(history):
        plt.figure()
        plt.xlabel('Epoch')
        plt.ylabel('Mean Abs Error [1000$]')
        plt.plot(history.epoch, np.array(history.history['mean_absolute_error']),
                 label='Train Loss')
        plt.plot(history.epoch, np.array(history.history['val_mean_absolute_error']),
                 label='Val loss')
        plt.legend()
        plt.ylim([0, 5])
 #      plt.show()



class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')