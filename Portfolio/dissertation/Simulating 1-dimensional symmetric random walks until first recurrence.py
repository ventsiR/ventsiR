import random

def timesOfRec(n):#This process has a chance of running indefinitely long
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

def avg(l):
    return sum(l)/len(l)

sample = timesOfRec(1000)
print(sample)
print(avg(sample))
print(max(sample))
print(sample.count(2)/len(sample))