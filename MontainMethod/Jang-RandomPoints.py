from math import dist
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

F = np.arange(0, 110, 20)
C = np.arange(0, 110, 20)

alpha = .054
beta = .054
M = np.zeros(shape=(F.shape[0], C.shape[0]))
sum = 0
for xindex in range(F.shape[0]):
    for yindex in range(C.shape[0]):
        for zindex in range(x.shape[0]):
            d = np.sqrt(((x.T[0, zindex] - F[xindex]) ** 2) + ((x.T[1, zindex] - C[yindex]) ** 2))
            m = np.exp(-alpha * d)
            M[yindex, xindex] += m
plotx = np.tile(F, (len(M), 1))
ploty = plotx.T
plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, M,
                cmap='viridis')
ax.grid(True)
plt.title("Montaña 1")
plt.show()

pfc = []
k = 0
M2 = np.zeros(shape=(F.shape[0], C.shape[0]))
MAc = []
delta = [0]
c0 = []
plt.figure()
while len(delta) < 4:
    c = np.max(M)
    for xindex in range(F.shape[0]):
        for yindex in range(C.shape[0]):
            if M[xindex, yindex] == c:
                pfc.append([xindex, yindex])
    for xindex in range(F.shape[0]):
        for yindex in range(C.shape[0]):
            g = 0
            for zindex in range(k + 1):
                dc = np.sqrt(((F[pfc[zindex][0]] - F[xindex]) ** 2) + ((F[pfc[zindex][1]] - C[yindex]) ** 2))
                g += np.exp(-beta * dc)
            mc = g
            val = M[xindex, yindex] - M[pfc[k][0], pfc[k][1]] * mc
            if val >= 0:
                M2[xindex, yindex] = val
            else:
                M2[xindex, yindex] = 0
    MAc.append(np.copy(M2))
    delta.append((c / np.max(M2)))
    M = np.copy(M2)
    c0.append([C[pfc[k][1]], F[pfc[k][0]]])
    plt.scatter(C[pfc[k][1]], F[pfc[k][0]], s=40, marker="D")
    k += 1
plt.scatter(x.T[0], x.T[1], s=10)
plt.grid(linewidth=1)
plt.show()
plotx = np.tile(F, (len(MAc[0]), 1))
ploty = plotx.T
plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, MAc[0],
                cmap='viridis')
ax.grid(True)
plt.title("Montaña 2")
plt.show()
plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, MAc[1],
                cmap='viridis')
ax.grid(True)
plt.title("Montaña 3")
plt.show()

c = np.array(c0)
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
        G[uindex] = np.sum(uvalues)
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
plt.scatter(c0[0][0], c0[0][1], s=40, color='r', marker="^", label="C1 init")
plt.scatter(cluster1[0], cluster1[1], s=10, color='r')
plt.scatter(c[1, 0], c[1, 1], s=40, color='b', marker="D", label="Cluster 2")
plt.scatter(c0[1][0], c0[1][1], s=40, color='b', marker="^", label="C2 init")
plt.scatter(cluster2[0], cluster2[1], s=10, color='b')
plt.scatter(c[2, 0], c[2, 1], s=40, color='g', marker="D", label="Cluster 3")
plt.scatter(c0[2][0], c0[2][1], s=40, color='g', marker="^", label="C3 init")
plt.scatter(cluster3[0], cluster3[1], s=10, color='g')
plt.legend()
plt.title("Jang")
plt.xlim([0, 100])
plt.ylim([0, 100])
plt.show()
