import random
from  matplotlib import pyplot as plt
import numpy as np

def twoDwalkGenerator(T):
    i = np.array([0,0])
    walkX = [0]
    walkY = [0]
    t = 1
    while t < T:   
        d = random.randint(0,3)
        if d == 0:
            d = np.array([-1,0])
        elif d == 1:
            d = np.array([1,0])
        elif d == 2:
            d = np.array([0,-1])
        else:
            d = np.array([0,1])
        i = i + d
        walkX.append(i[0])
        walkY.append(i[1])
        t=t+1
    return walkX, walkY

def plotTwoDWalk(T):
    Walk = twoDwalkGenerator(T)
    X = list(Walk[0])
    Y = list(Walk[1])
    gradUp = np.arange(0, (1+ 1/T), 1/T)
    gradDown = 1 - gradUp
    for i in range(0,T):
        plt.scatter(X[i], Y[i], color = (gradUp[i],gradDown[i],0))
    plt.plot(X,Y, color = (0,0,0))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

plotTwoDWalk(10)
plotTwoDWalk(100)
plotTwoDWalk(1000)
plotTwoDWalk(10000)