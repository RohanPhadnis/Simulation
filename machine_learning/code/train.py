import os
import time
import random
import json
import numpy
from tensorflow import keras

try:
    os.mkdir('../models')
except:
    pass
DIR = '../models/model{}'.format(time.time())
RATIO = 0.8
os.mkdir(DIR)
decoder = json.JSONDecoder()
xs = []
ys = []
val_xs = []
val_ys = []
with open('../data/data.txt') as file:
    text = file.read().split('\n')

random.shuffle(text)

for line in text[:len(text) * RATIO]:
    data = decoder.decode(line)
    xs.append(data[1])
    ys.append(data[0])

for line in text[len(text) * RATIO:]:
    data = decoder.decode(line)
    val_xs.append(data[1])
    val_ys.append(data[0])

xs = numpy.array(xs)
ys = numpy.array(ys)
val_xs = numpy.array(val_xs)
val_ys = numpy.array(val_ys)

tb = keras.callbacks.TensorBoard(logdir='{}/logs'.format(DIR))

model = keras.models.Sequential([
    keras.layers.Bidirectional(keras.layers.LSTM(32, return_sequences=True)),
    keras.layers.Bidirectional(keras.layers.LSTM(16)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(4)
])

model.summary()
model.compile(optimizer='adam', loss='mse', metrics='acc')
model.fit(x=xs, y=ys, epochs=100, verbose=1, callbacks=[tb], validation_data=(val_xs, val_ys))
model.save('{}/model.h5'.format(DIR))
