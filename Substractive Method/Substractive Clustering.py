from math import dist

import matplotlib.pyplot as plt
import numpy as np

x = np.array(
    [[0.36, 0.85], [0.65, 0.89], [0.62, 0.55], [0.50, 0.75], [0.35, 1.00], [0.90, 0.35], [1.00, 0.24], [0.99, 0.55],
     [0.83, 0.36], [0.88, 0.43]])
ra = .4
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
while len(Dc) < 2:
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
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.show()