import random
from  matplotlib import pyplot as plt
import numpy as np

def walkGenerator(T):
    i = 0
    walk = [0]
    t = 1
    while t < T:   
        d = random.randint(0,1)
        if d == 0:
            d = -1
        i = i + d
        walk.append(i)
        t=t+1
    return walk

def plotWalk(T):
    plt.plot(list(range(0,(T))), walkGenerator(T), [0]*T)
    plt.xlabel("Time")
    plt.ylabel("State")
    plt.show()

plotWalk(1000000)