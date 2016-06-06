import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def tobin(x):
    if x > .5:
        return 1
    else:
        return 0
