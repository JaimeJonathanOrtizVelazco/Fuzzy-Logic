from random import randint

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
U0 = np.zeros(shape=(3, 100))
for xval in range(0,100):
    randnum=randint(0,2)
    U0[randnum][xval] = 1
U = np.zeros(shape=U0.shape)
d = np.zeros(shape=(U0.shape))
m = 3
while True:
    opr1 = U0[0] ** 2 * x.T
    v1 = np.sum(opr1, axis=1) / np.sum(U0[0]**2)
    opr2 = U0[1] ** 2 * x.T
    v2 = np.sum(opr2, axis=1) / np.sum(U0[1]**2)
    opr3 = U0[2] ** 2 * x.T
    v3 = np.sum(opr3, axis=1) / np.sum(U0[2]**2)
    for xindex in range(x.shape[0]):
        d[0, xindex] = np.sqrt((x[xindex][0] - v1[0]) ** 2 + (x[xindex][1] - v1[1]) ** 2)
        d[1, xindex] = np.sqrt((x[xindex][0] - v2[0]) ** 2 + (x[xindex][1] - v2[1]) ** 2)
        d[2, xindex] = np.sqrt((x[xindex][0] - v3[0]) ** 2 + (x[xindex][1] - v3[1]) ** 2)
    for xindex in range(U.shape[0]):
        for kindex in range(U.shape[1]):
            for jindex in range(d.shape[0]):
                U[xindex, kindex] += (d[xindex, kindex] / d[jindex, kindex]) ** (2 / (m - 1))
            U[xindex, kindex] = U[xindex, kindex] ** -1
    Val=np.sum((U0-U)**2,axis=0)
    Val=np.sum(Val,axis=0)
    if (Val>=0.005):
        U0 = U
        U = np.zeros(shape=U0.shape)
    else:
        break
U=np.around(U)
cluster1 = np.round(x.T * U[0])
cluster2 = np.round(x.T * U[1])
cluster3 = np.round(x.T * U[2])
notvalue = np.array(np.where(cluster1[0] == 0))
cluster1 = np.array(np.delete(cluster1, notvalue, axis=1))
notvalue = np.array(np.where(cluster2[0] == 0))
cluster2 = np.array(np.delete(cluster2, notvalue, axis=1))
notvalue = np.array(np.where(cluster3[0] == 0))
cluster3 = np.array(np.delete(cluster3, notvalue, axis=1))
plt.figure()
plt.scatter(cluster1[0], cluster1[1], s=10, color='r')
plt.scatter(v1[0], v1[1], s=40, color='r', marker="D", label="Cluster 1")
plt.scatter(cluster2[0], cluster2[1], s=10, color='b')
plt.scatter(v2[0], v2[1], s=40, color='b', marker="D", label="Cluster 2")
plt.scatter(cluster3[0], cluster3[1], s=10, color='g')
plt.scatter(v3[0], v3[1], s=40, color='g', marker="D", label="Cluster 3")
plt.legend()
plt.title("Ponse CMeans")
plt.show()
