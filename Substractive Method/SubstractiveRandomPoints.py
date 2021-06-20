from math import dist
from random import sample, randint
import matplotlib.pyplot as plt
import numpy as np
x = []
for val in range(0, 35):
    xnum = randint(0, 40)
    ynum = randint(60, 100)
    x.append([xnum, ynum])
for val in range(0, 40):
    xnum = randint(30, 60)
    ynum = randint(0, 40)
    x.append([xnum, ynum])
for val in range(0, 25):
    xnum = randint(70, 100)
    ynum = randint(50, 90)
    x.append([xnum, ynum])
x = np.array(x)
ra = 40
rb = 1.5 * ra
D = np.zeros(shape=x.shape[0])
Dc = []
xc = []
k = 0
for index, xvalue in enumerate(x):
    for jvalue in x:
        D[index] += np.exp(-(dist(xvalue, jvalue) ** 2) / ((ra / 2) ** 2))
Dc.append(np.amax(D))
xc.append(x[np.where(D == Dc[k])[0]][0])
while len(Dc) < 3:
    print(xc[k][0])
    for index, xvalue in enumerate(x):
        D[index] -= Dc[k] * np.exp(-(dist(xvalue, xc[k]) ** 2) / ((rb / 2) ** 2))
    Dc.append(np.amax(D))
    k += 1
    xc.append(x[np.where(D == Dc[k])[0]][0])
xc=np.array(xc)
plt.figure(num=1)
plt.scatter(x.T[0], x.T[1])
plt.scatter(xc.T[0],xc.T[1])
plt.xlim([0, 100])
plt.ylim([0, 100])
plt.show()