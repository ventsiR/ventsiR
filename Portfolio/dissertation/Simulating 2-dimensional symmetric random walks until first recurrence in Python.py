import random
import numpy as np

def timesOfRec(n):#This process has a chance of running indefinitely long
    j = 1
    tTaken = []
    while j <= n:
        i= np.array([0,0])
        i0 = random.randint(0,3)
        if (i0 == 0):
            i = np.array([-1,0])
        elif(i0 == 1):
            i = np.array([1,0])
        elif(i0 == 2):
            i = np.array([0,-1])
        else:
            i = np.array([0,1])
        t = 1
        while i[0] != 0 or i[1] != 0:
            d0 = random.randint(0,3)
            if (d0 == 0):
                d = np.array([-1,0])
            elif(d0 == 1):
                d = np.array([1,0])
            elif(d0 == 2):
                d = np.array([0,-1])
            else:
                d = np.array([0,1])
            i = i + d
            t = t + 1
        tTaken.append(t)
        j = j + 1
    return tTaken

print(timesOfRec(1))