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
d = np.zeros(shape=U0.T.shape)
v1val = True
v2val = True
v3val = True
v1in=0
v2in=0
v3in=0
while True:
    opr1 = U0[0] * x.T
    v1 = np.sum(opr1, axis=1) / np.sum(U0[0])
    if v1val:
        v1in = v1
        v1val = False
    opr2 = U0[1] * x.T
    v2 = np.sum(opr2, axis=1) / np.sum(U0[1])
    if v2val:
        v2in = v2
        v2val = False
    opr3 = U0[2] * x.T
    v3 = np.sum(opr3, axis=1) / np.sum(U0[2])
    if v3val:
        v3in = v3
        v3val = False
    for xindex in range(x.shape[0]):
        d[xindex, 0] = np.sqrt((x[xindex][0] - v1[0]) ** 2 + (x[xindex][1] - v1[1]) ** 2)
        d[xindex, 1] = np.sqrt((x[xindex][0] - v2[0]) ** 2 + (x[xindex][1] - v2[1]) ** 2)
        d[xindex, 2] = np.sqrt((x[xindex][0] - v3[0]) ** 2 + (x[xindex][1] - v3[1]) ** 2)
    k = np.amin(d, axis=1)
    for xindex in range(x.shape[0]):
        if k[xindex] == d[xindex][0]:
            U[0, xindex] = 1
        else:
            U[0, xindex] = 0
        if k[xindex] == d[xindex][1]:
            U[1, xindex] = 1
        else:
            U[1, xindex] = 0
        if k[xindex] == d[xindex][2]:
            U[2, xindex] = 1
        else:
            U[2, xindex] = 0
    if (not np.array_equal(U, U0)):
        U0 = U
        U = np.zeros(shape=U0.shape)
    else:
        break
cluster1 = x.T * U[0]
cluster2 = x.T * U[1]
cluster3 = x.T * U[2]
plt.figure()
plt.scatter(cluster1[0], cluster1[1], s=10, color='r')
plt.scatter(v1[0], v1[1], s=40, color='r', marker="D", label="Cluster 1")
plt.scatter(v1in[0], v1in[1], s=40, color='r', marker="^", label="C1 init")
plt.scatter(cluster2[0], cluster2[1], s=10, color='b')
plt.scatter(v2[0], v2[1], s=40, color='b', marker="D", label="Cluster 2")
plt.scatter(v2in[0], v2in[1], s=40, color='b', marker="^", label="C2 init")
plt.scatter(cluster3[0], cluster3[1], s=10, color='g')
plt.scatter(v3[0], v3[1], s=40, color='g', marker="D", label="Cluster 3")
plt.scatter(v3in[0], v3in[1], s=40, color='g', marker="^", label="C3 init")
plt.legend()
plt.title("Ponse")
plt.xlim([0, 100])
plt.ylim([0, 100])
plt.show()
