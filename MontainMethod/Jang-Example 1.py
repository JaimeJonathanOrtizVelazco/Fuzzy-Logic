import matplotlib.pyplot as plt
import numpy as np

x = np.array(
    [[0.36, 0.85], [0.65, 0.89], [0.62, 0.55], [0.50, 0.75], [0.35, 1.00], [0.90, 0.35], [1.00, 0.24], [0.99, 0.55],
     [0.83, 0.36], [0.88, 0.43]])

F = np.arange(0, max(x.T[0] + 0.2), 0.2)
C = np.arange(0, max(x.T[1] + 0.2), 0.2)

alpha = 5.4
beta = 5.4
M = np.zeros(shape=(F.shape[0], C.shape[0]))
sum = 0
for xindex in range(F.shape[0]):
    for yindex in range(C.shape[0]):
        for zindex in range(x.shape[0]):
            d = np.sqrt(((x[zindex, 0] - F[xindex]) ** 2) + ((x[zindex, 1] - C[yindex]) ** 2))
            m = np.exp(-alpha * d)
            M[yindex, xindex] = sum + m
            sum = M[yindex, xindex]
        sum = 0
plotx = np.tile(F, (len(M), 1))
ploty = plotx.T
plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, M,
                cmap='viridis')
ax.grid(True)
plt.show()

pfc = []
k = 0
M2 = np.zeros(shape=(F.shape[0], C.shape[0]))
MAc = []
delta = []
plt.figure()
while len(delta) < 2:
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
    plt.scatter(C[pfc[k][1]], F[pfc[k][0]])
    k += 1
plt.scatter(x.T[0], x.T[1])
plt.xlim([0, 1])
plt.ylabel([0, 1])
plt.grid(linewidth=0.2)
plt.show()
plotx = np.tile(F, (len(MAc[0]), 1))
ploty = plotx.T
plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, MAc[0],
                cmap='viridis')
ax.grid(True)
plt.show()
