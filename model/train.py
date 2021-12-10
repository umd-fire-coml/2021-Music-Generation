from keras.callbacks import ModelCheckpoint

import tensorflow as tf
import datetime

from data_prep import prepare
from model import createModel
from clean import cleanup
from os.path import exists


def train_model(network_input, network_output, model, filepath):
    checkpoint = ModelCheckpoint(
        filepath, monitor='loss', 
        verbose=0,        
        save_best_only=True,        
        mode='min'
    )

    log_dir = "model/logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    callbacks_list = [checkpoint, tensorboard_callback]     
    model.fit(network_input, network_output, epochs=100, batch_size=25, callbacks=callbacks_list)
    cleanup()