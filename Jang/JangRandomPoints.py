from math import dist
from random import randint
from random import sample
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
c0 = np.array(sample(x.tolist(), k=3))
c = np.copy(c0)
plt.figure()
U = np.zeros(shape=(c.shape[0], x.shape[0]))
U0 = np.zeros(shape=(c.shape[0], x.shape[0]))
while True:
    for i in range(U.shape[0]):
        for j in range(U.shape[1]):
            flag = 0
            for k in range(c.shape[0]):
                if i != k:
                    if dist(x[j], c[i]) ** 2 <= dist(x[j], c[k]) ** 2:
                        flag = 1
                    else:
                        flag = 0
                        break
            U[i, j] = flag
    G = np.zeros(U.shape[0])
    for uindex, uvalues in enumerate(U):
        G[uindex] = sum(uvalues)
    for uindex, uvalue in enumerate(U):
        c[uindex] = np.sum(x.T * uvalue, axis=1) / G[uindex]
    if (np.array_equal(U0, U)):
        break
    else:
        U0 = U
        U = np.zeros(shape=(c.shape[0], x.shape[0]))
cluster1 = x.T * U[0]
cluster2 = x.T * U[1]
cluster3 = x.T * U[2]
plt.figure()
plt.scatter(c[0, 0], c[0, 1], s=40, color='r', marker="D", label="Cluster 1")
plt.scatter(c0[0, 0], c0[0, 1], s=40, color='r', marker="^", label="C1 init")
plt.scatter(cluster1[0], cluster1[1], s=10, color='r')
plt.scatter(c[1, 0], c[1, 1], s=40, color='b', marker="D", label="Cluster 2")
plt.scatter(c0[1, 0], c0[1, 1], s=40, color='b', marker="^", label="C2 init")
plt.scatter(cluster2[0], cluster2[1], s=10, color='b')
plt.scatter(c[2, 0], c[2, 1], s=40, color='g', marker="D", label="Cluster 3")
plt.scatter(c0[2, 0], c0[2, 1], s=40, color='g', marker="^", label="C3 init")
plt.scatter(cluster3[0], cluster3[1], s=10, color='g')
plt.legend()
plt.title("Jang")
plt.xlim([0, 100])
plt.ylim([0, 100])
plt.show()
