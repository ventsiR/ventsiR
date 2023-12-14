import random
from matplotlib import pyplot as plt
import numpy as np

def arbitraryTriangleChaosGame(m):
    a = []
    a.append(np.array([random.randint(0,1000000)/1000000,random.randint(0,1000000)/1000000]))
    plt.scatter(a[0][0], a[0][1], c="black")
    x = []
    for i in range(0,3):
        x.append(np.array([random.randint(0,1000000)/1000000,random.randint(0,1000000)/1000000]))
        plt.scatter(x[i][0], x[i][1], c="blue")
    for i in range(0,m):
        p = random.randint(0,2)
        a.append(a[i] + ((1/2)*(x[p][0] - a[i][0]), (1/2)*(x[p][1] - a[i][1])))
        plt.scatter(a[i+1][0], a[i+1][1], c="black", s = 1)
    plt.show()

def eqltrlTriangleChaosGame(m):
    a = []
    a.append(np.array([random.randint(0,1000000)/1000000,random.randint(0,1000000)/1000000]))
    plt.scatter(a[0][0], a[0][1], c="black")
    x = []
    x.append(np.array([0,0]))
    plt.scatter(x[0][0], x[0][1], c="blue")
    x.append(np.array([1,0]))
    plt.scatter(x[1][0], x[1][1], c="blue")
    x.append(np.array([0.5,1]))
    plt.scatter(x[2][0], x[2][1], c="blue")
    for i in range(0,m):
        p = random.randint(0,2)
        a.append(a[i] + ((1/2)*(x[p][0] - a[i][0]), (1/2)*(x[p][1] - a[i][1])))
        plt.scatter(a[i+1][0], a[i+1][1], c="black", s = 1)
    plt.show()

def twoDnGonChaosGame(n0,m0):
    n = int(np.ceil(abs(n0)))
    m = int(np.ceil(abs(m0)))
    a = []
    a.append(np.array([random.randint(-500000,500000)/1000000,random.randint(-500000,500000)/1000000]))
    plt.scatter(a[0][0], a[0][1], c="black")
    x = []
    if n == 0:
        print("Entry cannot be zero!")
    else:
        theta = 2*np.pi / n
        r = 1/(2*np.cos(theta/2))
        for i in range(0,n):
            x.append(np.array([-r*np.sin((i+(1/2))*theta), r*np.cos((i+(1/2))*theta)]))
            plt.scatter(x[i][0], x[i][1], c="blue")
    for i in range(0,m):
        p = random.randint(0,n-1)
        a.append(a[i] + ((1/2)*(x[p][0] - a[i][0]), (1/2)*(x[p][1] - a[i][1])))
        plt.scatter(a[i+1][0], a[i+1][1], c="black", s = 1)
    plt.show()

def fern(n):
    a = []
    a.append(np.array([0,0]))
    for i in range(0,n):
        r = random.randint(0,99)
        if r < 1:
            a.append(np.array([0,0.16*a[i][1]]))
            plt.scatter(a[i+1][0], a[i+1][1], c="green", s = 1)
        elif r < 86:
            a.append(np.array([0.85*a[i][0] + 0.04*a[i][1],-0.04*a[i][0] + 0.85*a[i][1] + 1.6]))
            plt.scatter(a[i+1][0], a[i+1][1], c="green", s = 1)            
        elif r < 93:
            a.append(np.array([0.2 * a[i][0] - 0.26 * a[i][1],0.23 * a[i][0] + 0.22 * a[i][1] + 1.6]))
            plt.scatter(a[i+1][0], a[i+1][1], c="green", s = 1)
        else:
            a.append(np.array([-0.15 * a[i][0] + 0.28 * a[i][1],0.26 * a[i][0] + 0.24 * a[i][1] + 0.44]))
            plt.scatter(a[i+1][0], a[i+1][1], c="green", s = 1)
    plt.show()

arbitraryTriangleChaosGame(100)
# twoDnGonChaosGame(3, 3000)
# fern(1000)



