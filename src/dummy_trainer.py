# edit this file to create a simple model trainer for your dataset and model.
from os import path
from tensorflow import keras
from tensorflow.keras.callbacks import ModelCheckpoint
from os.path import exists

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
history = model.fit(
    dataset.x_train,
    dataset.y_train,
    batch_size=64,
    epochs=2,
    # We pass some validation for
    # monitoring validation loss and metrics
    # at the end of each epoch
    validation_data=(dataset.x_val, dataset.y_val),
    callbacks=[mc]
)