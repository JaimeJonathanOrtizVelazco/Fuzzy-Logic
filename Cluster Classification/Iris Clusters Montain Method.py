from math import dist

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("IrisDataBase.csv", sep="\t", names=["Data 1", "Data 2", "Data 3", "Data 4", "Tipo"])
data[["Data 1", "Data 2", "Data 3", "Data 4"]] = data[["Data 1", "Data 2", "Data 3", "Data 4"]].astype(float, copy=True)
x = data[["Data 2", "Data 3", "Data 4"]].values
F = np.arange(0, 6, 1.5)
C = np.arange(0, 8, 2)
D = np.arange(0, 4, 1)
alpha = 5.4
beta = 5.4
M = np.zeros(shape=(F.shape[0], C.shape[0], D.shape[0]))
sum = 0
for xindex in range(F.shape[0]):
    for yindex in range(C.shape[0]):
        for dindex in range(D.shape[0]):
            for zindex in range(x.shape[0]):
                d = np.sqrt(((x.T[0, zindex] - F[xindex]) ** 2) + ((x.T[1, zindex] - C[yindex]) ** 2) + (
                        (x.T[2, zindex] - D[dindex]) ** 2))
                m = np.exp(-alpha * d)
                M[xindex, yindex, dindex] = sum + m
                sum = M[xindex, yindex, dindex]
            sum = 0
pfc = []
k = 0
M2 = np.zeros(shape=(F.shape[0], C.shape[0], D.shape[0]))
MAc = []
delta = [0]
c0 = []
fig = plt.figure()
ax = plt.axes(projection="3d")
c = []
while delta[k] < 3:
    c.append(np.max(M))
    for xindex in range(F.shape[0]):
        for yindex in range(C.shape[0]):
            for dindex in range(D.shape[0]):
                if M[xindex, yindex, dindex] == c[k]:
                    pfc.append([xindex, yindex, dindex])
    for xindex in range(F.shape[0]):
        for yindex in range(C.shape[0]):
            for dindex in range(D.shape[0]):
                g = 0
                for zindex in range(k + 1):
                    dc = np.sqrt(((F[pfc[zindex][0]] - F[xindex]) ** 2) + ((C[pfc[zindex][1]] - C[yindex]) ** 2) + (
                            (D[pfc[zindex][2]] - D[dindex]) ** 2))
                    g += np.exp(-beta * dc)
                val = M[xindex, yindex, dindex] - M[pfc[k][0], pfc[k][1], pfc[k][2]] * g
                if val >= 0:
                    M2[xindex, yindex, dindex] = val
                else:
                    M2[xindex, yindex, dindex] = 0
    MAc.append(np.copy(M2))
    delta.append((c[0] / np.max(M2)))
    M = np.copy(M2)
    c0.append([F[pfc[k][0]], C[pfc[k][1]], D[pfc[k][2]]])
    ax.scatter3D(F[pfc[k][0]], C[pfc[k][1]], D[pfc[k][2]], s=40, marker="D")
    k += 1
ax.scatter(x.T[0], x.T[1], x.T[2], s=10)
plt.grid(linewidth=1)
plt.title("Mountain clustrs location")
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
notvalue = np.array(np.where(cluster1[0] == 0))
cluster1 = np.array(np.delete(cluster1, notvalue, axis=1))
notvalue = np.array(np.where(cluster2[0] == 0))
cluster2 = np.array(np.delete(cluster2, notvalue, axis=1))
notvalue = np.array(np.where(cluster3[0] == 0))
cluster3 = np.array(np.delete(cluster3, notvalue, axis=1))
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter3D(c[0, 0], c[0, 1], c[0, 2], s=40, color='r', marker="^", label="Cluster 1")
ax.scatter3D(c0[0][0], c0[0][1], c0[0][2], s=40, color='r', marker="D", label="C1 init")
ax.scatter3D(cluster1[0], cluster1[1], cluster1[2], s=10, color='r')
ax.scatter3D(c[1, 0], c[1, 1], c[1, 2], s=40, color='b', marker="^", label="Cluster 2")
ax.scatter3D(c0[1][0], c0[1][1], c0[1][2], s=40, color='b', marker="D", label="C2 init")
ax.scatter3D(cluster2[0], cluster2[1], cluster2[2], s=10, color='b')
ax.scatter3D(c[2, 0], c[2, 1], c[2, 2], s=40, color='g', marker="^", label="Cluster 3")
ax.scatter3D(c0[2][0], c0[2][1], c0[2][2], s=40, color='g', marker="D", label="C3 init")
ax.scatter3D(cluster3[0], cluster3[1], cluster3[2], s=10, color='g')
plt.legend()
plt.title("Jang")
plt.show()
