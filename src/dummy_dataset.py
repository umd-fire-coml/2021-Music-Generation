import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class MyDataset(object):
    def __init__(self):
        (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

        # Preprocess the data (these are NumPy arrays)
        x_train = x_train.reshape(60000, 784).astype("float32") / 255
        x_test = x_test.reshape(10000, 784).astype("float32") / 255

        y_train = y_train.astype("float32")
        y_test = y_test.astype("float32")

        # Reserve 10,000 samples for validation
        self.x_val = x_train[-10000:]
        self.y_val = y_train[-10000:]
        self.x_train = x_train[:-10000]
        self.y_train = y_train[:-10000]