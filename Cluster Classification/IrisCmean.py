from random import sample, randint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

numclusters = 4
data = pd.read_csv("IrisDataBase.csv", sep="\t", names=["Data 1", "Data 2", "Data 3", "Data 4", "Tipo"])
data[["Data 1", "Data 2", "Data 3", "Data 4"]] = data[["Data 1", "Data 2", "Data 3", "Data 4"]].astype(float, copy=True)
x = data[["Data 2", "Data 3", "Data 4"]].values
dataClas = []
for dataval in data.values:
    if dataval[4] == 'Iris-setosa ':
        dataClas.append([dataval[1], dataval[2], dataval[3]])
    elif dataval[4] == 'Iris-versicolor ':
        dataClas.append([dataval[1], dataval[2], dataval[3]])
    elif dataval[4] == 'Iris-virginica ':
        dataClas.append([dataval[1], dataval[2], dataval[3]])
x = np.array(dataClas)
U0 = np.zeros(shape=(numclusters, data.shape[0]))
for xval in range(0, data.shape[0]):
    randnum = randint(0, numclusters - 1)
    U0[randnum][xval] = 1
U = np.zeros(shape=U0.shape)
d = np.zeros(shape=(U0.shape))
m = 2
opr = np.zeros(shape=(numclusters, x.T.shape[0], x.T.shape[1]))
v = np.zeros(shape=(numclusters, x.T.shape[0]))
while True:
    for clus in range(numclusters):
        opr[clus] = (U0[clus] ** 2) * x.T
        v[clus] = np.sum(opr[clus], axis=1) / np.sum(U0[clus] ** 2)
    for xindex in range(x.shape[0]):
        for clus in range(numclusters):
            vald = 0
            for dims in range(x.T.shape[0]):
                vald += (x[xindex][dims] - v[clus][dims]) ** 2
            d[clus, xindex] = np.sqrt(vald)
    for xindex in range(U.shape[0]):
        for kindex in range(U.shape[1]):
            for jindex in range(d.shape[0]):
                U[xindex, kindex] += (d[xindex, kindex] / d[jindex, kindex]) ** (2 / (m - 1))
            U[xindex, kindex] = U[xindex, kindex] ** -1
    Val = np.sum((U0 - U) ** 2, axis=0)
    Val = np.sum(Val, axis=0)
    if Val >= 0.005:
        U0 = U
        U = np.zeros(shape=U0.shape)
    else:
        break
U = np.around(U)
clusters = np.zeros(shape=(numclusters, x.T.shape[0], x.T.shape[1]))
clustersfre = []
for clus in range(numclusters):
    clusters[clus] = U[clus] * x.T
    notvalue = np.array(np.where(clusters[clus] == 0))
    clustersfre.append(np.array(np.delete(clusters[clus], notvalue, axis=1)))
clustercolors = ['r', 'b', 'g', 'y']
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter3D(v[0][0], v[0][1], v[0][2], s=40, color='r', marker="D", label="Cluster 1")
ax.scatter3D(clustersfre[0][0], clustersfre[0][1], clustersfre[0][2], s=10, color='r')
ax.scatter3D(v[1][0], v[1][1], v[1][2], s=40, color='b', marker="D", label="Cluster 2")
ax.scatter3D(clustersfre[1][0], clustersfre[1][1], clustersfre[1][2], s=10, color='b')
ax.scatter3D(v[2][0], v[2][1], v[2][2], s=40, color='g', marker="D", label="Cluster 3")
ax.scatter3D(clustersfre[2][0], clustersfre[2][1], clustersfre[2][2], s=10, color='g')
ax.scatter3D(v[3][0], v[3][1], v[3][2], s=40, color='y', marker="D", label="Cluster 4")
ax.scatter3D(clustersfre[3][0], clustersfre[3][1], clustersfre[3][2], s=10, color='y')
plt.legend()
plt.title("Iris CMeans")
plt.show()
