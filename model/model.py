from keras.engine.sequential import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation

def createModel():

    model = Sequential()
    model.add(LSTM(
        256,
        input_shape=(100, 1),
        return_sequences=True
    ))
    model.add(Dropout(0.3))
    model.add(LSTM(512, return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(256))
    model.add(Dense(256))
    model.add(Dropout(0.3))
    # 303 -> n_vocab
    model.add(Dense(303))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    return model