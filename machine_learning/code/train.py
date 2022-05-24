import os
import time
import random
import json
import numpy
from tensorflow import keras
import tensorflow as tf

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

text = text[:len(text)-1]
random.shuffle(text)

for line in text[:int(len(text) * RATIO)]:
    data = decoder.decode(line)
    l = []
    for element in data[1]:
        l.append(element[1])
    xs.append(l)
    ys.append(data[0][0])

for line in text[int(len(text) * RATIO):]:
    data = decoder.decode(line)
    l = []
    for element in data[1]:
        l.append(element[1])
    val_xs.append(l)
    val_ys.append(data[0][0])

xs = numpy.array(xs)
ys = numpy.array(ys)
val_xs = numpy.array(val_xs)
val_ys = numpy.array(val_ys)

print('train x shape:', xs.shape)
print('val x shape:', val_xs.shape)
print('train y shape:', ys.shape)
print('val y shape:', val_ys.shape)

tb = keras.callbacks.TensorBoard(log_dir='{}/logs'.format(DIR))

model = keras.models.Sequential([
    # keras.layers.Conv1D(filters=64, kernel_size=3, activation='relu', padding='causal', input_shape=(100, 2)),
    # keras.layers.LSTM(32),
    # keras.layers.Flatten(input_shape=(100, 2)),
    keras.layers.Lambda(lambda x: tf.expand_dims(x, axis=-1), input_shape=(100,)),
    keras.layers.Conv1D(filters=32, kernel_size=5, activation='relu'),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(8, activation='relu'),
    keras.layers.Dense(1)
])

model.summary()
model.compile(optimizer='RMSprop', loss='huber', metrics='acc')
model.fit(x=xs, y=ys, epochs=100, verbose=1, callbacks=[tb], validation_data=(val_xs, val_ys))
model.save('{}/model.h5'.format(DIR))
