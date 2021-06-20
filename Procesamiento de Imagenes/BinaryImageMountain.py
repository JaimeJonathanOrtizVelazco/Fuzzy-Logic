from math import dist

import numpy as np
from matplotlib import pyplot as plt
from skimage import io
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from skimage.transform import resize

img = io.imread('Im4.jpg')
img = rgb2gray(img)
img = resize(img, (480, 640), anti_aliasing=True)
plt.figure()
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
thresh = threshold_otsu(img)
binarize = img < thresh
plt.figure()
plt.imshow(binarize, cmap=plt.cm.gray)
plt.show()
x = []
for yindex in range(binarize.shape[0]):
    for xindex in range(binarize.shape[1]):
        if binarize[yindex, xindex]:
            x.append([xindex, yindex])
x = np.array(x)
F = np.arange(0, 640, 128)
C = np.arange(0, 480, 96)
alpha = .0090
beta = .0090
M = np.zeros(shape=(F.shape[0], C.shape[0]))
for xindex in range(F.shape[0]):
    for yindex in range(C.shape[0]):
        for zindex in range(x.shape[0]):
            d = np.sqrt(((x.T[0, zindex] - F[xindex]) ** 2) + ((x.T[1, zindex] - C[yindex]) ** 2))
            m = np.exp(-alpha * d)
            M[yindex, xindex] += m
plotx = np.tile(F, (C.shape[0], 1))
ploty = np.tile(C.T, (F.shape[0], 1)).T
plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, M,
                cmap='viridis')
ax.grid(True)
plt.title("Montaña 1")
plt.show()
#
k = 0
M2 = np.zeros(shape=M.shape)
MAc = []
pfc = []
delta = [0]
c0 = []
c = []
while len(delta) <= 5:
    c.append(np.max(M))
    for xindex in range(F.shape[0]):
        for yindex in range(C.shape[0]):
            if M[xindex, yindex] == c[k]:
                if len(pfc) == k:
                    pfc.append([xindex, yindex])
                else:
                    pfc[k] = [xindex, yindex]
    for xindex in range(F.shape[0]):
        for yindex in range(C.shape[0]):
            g = 0
            for zindex in range(k + 1):
                dc = np.sqrt(((F[pfc[zindex][0]] - F[xindex]) ** 2) + ((F[pfc[zindex][1]] - C[yindex]) ** 2))
                g += np.exp(-beta * dc)
            val = M[xindex, yindex] - M[pfc[k][0], pfc[k][1]] * g
            if val >= 0:
                M2[xindex, yindex] = val
            else:
                M2[xindex, yindex] = 0
    MAc.append(np.copy(M2))
    delta.append(c[0] / np.max(M2))
    M = np.copy(M2)
    c0.append([F[pfc[k][0]], C[pfc[k][1]]])
    k += 1
c0 = np.array(c0)
plt.figure()
plt.scatter(x.T[0], x.T[1], s=10)
plt.scatter(c0.T[0], c0.T[1], s=40, marker="D")
plt.grid(linewidth=1)
plt.show()
for xindex in range(len(pfc)):
    plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(plotx, ploty, MAc[xindex], cmap='viridis')
    ax.grid(True)
    plt.title("Montaña {}".format(xindex))
    plt.show()

U = np.zeros(shape=(c0.shape[0], x.shape[0]))
U0 = np.zeros(shape=(c0.shape[0], x.shape[0]))
while True:
    for i in range(U.shape[0]):
        for j in range(U.shape[1]):
            flag = 0
            for k in range(c0.shape[0]):
                if i != k:
                    if dist(x[j], c0[i]) ** 2 <= dist(x[j], c0[k]) ** 2:
                        flag = 1
                    else:
                        flag = 0
                        break
            U[i, j] = flag
    G = np.zeros(U.shape[0])
    for uindex, uvalues in enumerate(U):
        G[uindex] = np.sum(uvalues)
    for uindex, uvalue in enumerate(U):
        c0[uindex] = np.sum(x.T * uvalue, axis=1) / G[uindex]
    if (np.array_equal(U0, U)):
        break
    else:
        U0 = U
        U = np.zeros(shape=(c0.shape[0], x.shape[0]))
cluster1 = x.T * U[0]
cluster2 = x.T * U[1]
cluster3 = x.T * U[2]
cluster4 = x.T * U[3]
cluster5 = x.T * U[4]
plt.figure()
plt.scatter(cluster1[0], cluster1[1], s=10, color='r')
plt.scatter(cluster2[0], cluster2[1], s=10, color='b')
plt.scatter(cluster3[0], cluster3[1], s=10, color='g')
plt.scatter(cluster4[0], cluster4[1], s=10, color='y')
plt.scatter(cluster5[0], cluster5[1], s=10, color='c')
plt.scatter(c0.T[0], c0.T[1], s=40, marker="D")
plt.title("Jang")
plt.show()
