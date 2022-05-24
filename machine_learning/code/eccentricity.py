import json
# import numpy
# from scipy.optimize import curve_fit


# function = lambda t, e, d, p: e * p / (1 + e * numpy.sin(t - p))


def mean_absolute_error(data):
    mean = sum([abs(num) for num in data]) / len(data)
    total = 0
    for num in data:
        total += abs(mean - num) / mean
    return total / len(data)


decoder = json.JSONDecoder()

with open('../data/data.txt') as file:
    text = file.read()

text = text.split('\n')[:-1]
for line in text:
    l = decoder.decode(line)
    l2 = [num_list[1] for num_list in l[1]]
    # ts = [num_list[0] for num_list in l[1]]
    print(l[0][0], mean_absolute_error(l2))
