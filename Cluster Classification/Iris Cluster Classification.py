from math import dist
from random import sample
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("IrisDataBase.csv", sep="\t", names=["Data 1", "Data 2", "Data 3", "Data 4", "Tipo"])
data[["Data 1", "Data 2", "Data 3", "Data 4"]] = data[["Data 1", "Data 2", "Data 3", "Data 4"]].astype(float, copy=True)
x = data[["Data 2", "Data 3", "Data 4"]].values
dataClas = [[], [], []]
for dataval in data.values:
    if (dataval[4] == 'Iris-setosa '):
        dataClas[0].append([dataval[1], dataval[2], dataval[3]])
    elif (dataval[4] == 'Iris-versicolor '):
        dataClas[1].append([dataval[1], dataval[2], dataval[3]])
    elif (dataval[4] == 'Iris-virginica '):
        dataClas[2].append([dataval[1], dataval[2], dataval[3]])
dataClas = np.array(dataClas)
dataClas = tuple(dataClas.tolist())
c0 = np.array(sample(x.tolist(), k=3))
c = np.copy(c0)
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
notvalue = np.array(np.where(cluster1[0] == 0))
cluster1 = np.array(np.delete(cluster1, notvalue, axis=1))
notvalue = np.array(np.where(cluster2[0] == 0))
cluster2 = np.array(np.delete(cluster2, notvalue, axis=1))
notvalue = np.array(np.where(cluster3[0] == 0))
cluster3 = np.array(np.delete(cluster3, notvalue, axis=1))
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter3D(c[0, 0], c[0, 1], c[0, 2], s=40, color='r', marker="D", label="Cluster 1")
ax.scatter3D(c0[0, 0], c0[0, 1], c0[0, 2], s=40, color='r', marker="^", label="C1 init")
ax.scatter3D(cluster1[0], cluster1[1], cluster1[2], s=10, color='r')
ax.scatter3D(c[1, 0], c[1, 1], c[1, 2], s=40, color='b', marker="D", label="Cluster 2")
ax.scatter3D(c0[1, 0], c0[1, 1], c0[1, 2], s=40, color='b', marker="^", label="C2 init")
ax.scatter3D(cluster2[0], cluster2[1], cluster2[2], s=10, color='b')
ax.scatter3D(c[2, 0], c[2, 1], c[2, 2], s=40, color='g', marker="D", label="Cluster 3")
ax.scatter3D(c0[2, 0], c0[2, 1], c0[2, 2], s=40, color='g', marker="^", label="C3 init")
ax.scatter3D(cluster3[0], cluster3[1], cluster3[2], s=10, color='g')
plt.legend()
plt.title("Jang")


def intersect(ls1: tuple, ls2: tuple):
    retunArra = []
    for valuel in ls1:
        if (ls2.__contains__(valuel)):
            retunArra.append(valuel)
    return len(retunArra)


Tipo = data['Tipo'].unique()
clust1count = []
clust2count = []
clust3count = []
clust1count.append(intersect(tuple(cluster1.T.tolist()), dataClas[0]))
clust1count.append(intersect(tuple(cluster1.T.tolist()), dataClas[1]))
clust1count.append(intersect(tuple(cluster1.T.tolist()), dataClas[2]))
clust2count.append(intersect(tuple(cluster2.T.tolist()), dataClas[0]))
clust2count.append(intersect(tuple(cluster2.T.tolist()), dataClas[1]))
clust2count.append(intersect(tuple(cluster2.T.tolist()), dataClas[2]))
clust3count.append(intersect(tuple(cluster3.T.tolist()), dataClas[0]))
clust3count.append(intersect(tuple(cluster3.T.tolist()), dataClas[1]))
clust3count.append(intersect(tuple(cluster3.T.tolist()), dataClas[2]))
maxinde1 = clust1count.index(max(clust1count))
maxinde2 = clust2count.index(max(clust2count))
maxinde3 = clust3count.index(max(clust3count))
valcus1 = 0
valcus2 = 0
valcus3 = 0
if (sum(clust1count) <= len(dataClas[0])):
    valcus1 = max(clust1count)
else:
    for index, valclus in enumerate(clust1count):
        if (index == maxinde1):
            valcus1 += valclus
        else:
            valcus1 -= valclus
if (sum(clust2count) <= len(dataClas[0])):
    valcus2 = max(clust2count)
else:
    for index, valclus in enumerate(clust2count):
        if (index == maxinde2):
            valcus2 += valclus
        else:
            valcus2 -= valclus
if (sum(clust3count) <= len(dataClas[0])):
    valcus3 = max(clust3count)
else:
    for index, valclus in enumerate(clust3count):
        if (index == maxinde3):
            valcus3 += valclus
        else:
            valcus3 -= valclus
print("El cluster uno pertenece al tipo", Tipo[maxinde1], "con una eficiencia de", (valcus1 * 100) / 50)
print("El cluster dos pertenece al tipo", Tipo[maxinde2], "con una eficiencia de", (valcus2 * 100) / 50)
print("El cluster tres pertenece al tipo", Tipo[maxinde3], "con una eficiencia de", (valcus3 * 100) / 50)
plt.show()
