import json
import numpy
from tensorflow import keras


decoder = json.JSONDecoder()
xs = []
ys = []
with open('../data/data.txt') as file:
    text = file.read().split('\n')
for y, x in text:
    ys.append(y)
    xs.append(x)

xs = numpy.array(xs)
ys = numpy.array(ys)


model = keras.models.Sequential([
    keras.layers.Dense(4)
])

model.summary()
model.compile(optimizer='adam', loss='mse')
model.fit(x=xs, y=ys, epochs=100)
