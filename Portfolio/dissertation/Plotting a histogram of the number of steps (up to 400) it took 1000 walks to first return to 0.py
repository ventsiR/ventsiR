import random
from  matplotlib import pyplot as plt
import numpy as np

def timesOfRec(n):
    j = 1
    tTaken = []
    while j <= n:
        i=0
        i0 = random.randint(0,1)
        if (i0 == 0):
            i = -1
        else:
            i = 1
        t = 1
        while i != 0:
            d0 = random.randint(0,1)
            if (d0 == 0):
                d = -1
            else:
                d = 1
            i = i + d
            t = t + 1
        tTaken.append(t)
        j = j + 1
    return tTaken

data = timesOfRec(1000)

bins = np.arange(0,400, 1)
plt.hist(data, bins=bins, alpha=1)
plt.xlabel("Number of steps until first recurrence")
plt.ylabel("Number of walks (out of 1000 total) which recurred in $x$ steps")
plt.show()