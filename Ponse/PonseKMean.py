import matplotlib.pyplot as plt
import numpy as np

x = np.array([[1, 1], [4, 1], [4, 2], [5.5, 1]])
print(x.shape[0])
plt.figure()
for xitem in x:
    plt.scatter(xitem[0], xitem[1])

U0 = np.array([[0, 0, 1, 1], [1, 1, 0, 0]])
U = np.zeros(shape=U0.shape)
d=np.zeros(shape=(x.shape))
while True:
    opr1 = U0[0] * x.T
    v1 = np.sum(opr1, axis=1) / np.sum(U0[0])
    opr2 = U0[1] * x.T
    v2 = np.sum(opr2, axis=1) / np.sum(U0[0])
    for xindex in range(x.shape[0]):
            d[xindex,0]=np.sqrt((x[xindex][0] - v1[0]) ** 2 + (x[xindex][1] - v1[1]) ** 2)
            d[xindex,1]=np.sqrt((x[xindex][0] - v2[0]) ** 2 + (x[xindex][1] - v2[1]) ** 2)
    k=np.amin(d,axis=1)
    for xindex in range(x.shape[0]):
        if k[xindex]==d[xindex][0]:
            U[0,xindex]=1
        else:
            U[0,xindex]=0
        if k[xindex]==d[xindex][1]:
            U[1,xindex]=1
        else:
            U[1,xindex]=0
    if (not np.array_equal(U, U0)):
        U0 = U
        U = np.zeros(shape=U0.shape)
    else:
        break

plt.figure()
plt.scatter(v1[0], v1[1])
plt.scatter(v2[0], v2[1])
plt.show()
