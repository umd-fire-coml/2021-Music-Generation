# edit this file to create a simple model trainer for your dataset and model.
from tensorflow import keras
from tensorflow.keras.callbacks import ModelCheckpoint
from os.path import exists

import numpy as np

from dummy_dataset import MyDataset
from dummy_model import my_model

dataset = MyDataset()

model = my_model()

model.compile(
    optimizer=keras.optimizers.RMSprop(learning_rate=1e-3),
    loss=keras.losses.SparseCategoricalCrossentropy(),
    metrics=[keras.metrics.SparseCategoricalAccuracy()],
)

mc=ModelCheckpoint('best_model.h5', monitor='val_loss', mode='min', save_best_only=True,verbose=1)

file_exists = exists('best_model.h5')

if file_exists is True:
    model.load_weights('best_model.h5')
    print('Weights Loaded!')

print("Fit model on training data")
    # We pass some validation for
    # monitoring validation loss and metrics
    # at the end of each epoch
history = model.fit(
    np.array(dataset.x_tr),
    np.array(dataset.y_tr),
    batch_size=128,
    epochs=50,
    validation_data=(np.array(dataset.x_val),np.array(dataset.y_val)),
    verbose=1,
    callbacks=[mc])