import os
import math
import random
import numpy
from tensorflow import keras

DIR = sorted(os.listdir('../models'))[-1]
model = keras.models.load_model('../models/{}/model.h5'.format(DIR))
calc = lambda t, e, d, p, c: ((e * d) / (1 + e * math.sin(t - p))) + c
ecc_determination = random.randint(0, 99)
circle_rad = 0
directrix = 10 ** ((random.random() + 0.5) * random.randint(2, 11))
phase_shift = random.random() * 2 * math.pi
if 0 <= ecc_determination < 2:
    eccentricity = 0
    circle_rad = 10 ** ((random.random() + 0.5) * random.randint(2, 11))
elif 2 <= ecc_determination < 4:
    eccentricity = 1
elif 4 <= ecc_determination < 52:
    eccentricity = random.random()
else:
    eccentricity = (1 + random.random()) * random.randint(1, 10)
l = [[eccentricity, directrix, phase_shift, circle_rad], []]
print(l[0])
start = random.random() * 2 * math.pi
step = (2 * math.pi - start) / 100
theta = start
j = 0
while theta < 2 * math.pi and j < 100:
    try:
        r = calc(theta, eccentricity, directrix, phase_shift, circle_rad)
        l[1].append([theta, r])
    except ZeroDivisionError:
        r = calc(theta - step/2, eccentricity, directrix, phase_shift, circle_rad)
        l[1].append([theta - step/2, r])
    theta += step
    j += 1

array = numpy.array([l[1]])
pred = model.predict(array)
print(pred)
