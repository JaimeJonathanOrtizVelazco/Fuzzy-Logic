import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

a1 = -0.3
c1 = 50
a2 = 0.3
c2 = 50
x = range(0, 101)
A1 = list(map(lambda x: 1 / (1 + np.exp(-a1 * (x - c1))), x))
A2 = list(map(lambda x: 1 / (1 + np.exp(-a2 * (x - c2))), x))
plt.plot(x, A1, x, A2)
plt.xlabel('X')
plt.ylabel('Membresia')
plt.show()

b1 = 25
sigma1 = 20
b2 = 75
sigma2 = 20
y = x
B1 = list(map(lambda y: np.exp(-0.5 * ((y - b1) / sigma1) ** 2), y))
B2 = list(map(lambda y: np.exp(-0.5 * ((y - b2) / sigma2) ** 2), y))
plt.plot(y, B1, y, B2)
plt.xlabel('Y')
plt.ylabel('Membresia')
plt.show()

sa1 = -0.3
sc1 = 50
sc2 = 75
ssigma2 = 20
z = x
C1 = list(map(lambda z: 1 / (1 + np.exp(-sa1 * (z - sc1))), z))
C2 = list(map(lambda z: np.exp(-0.5 * ((z - sc2) / ssigma2) ** 2), z))
plt.plot(z, C1, z, C2)
plt.xlabel('Z')
plt.ylabel('Membresia')
plt.show()

x1 = 60
y1 = 35
X = round(x1)
Y = round(y1)
MFX = [A1[X], A2[X]]
MFY = [B1[Y], B2[Y]]
R1 = min(MFX[0], MFY[0])
R2 = min(MFX[0], MFY[1])
R3 = min(MFX[1], MFY[0])
R4 = min(MFX[1], MFY[1])
Corte1 = max(R1, R2)
Corte2 = max(R3, R4)

C1 = [x if x < Corte1 else Corte1 for x in C1]
C2 = [x if x < Corte2 else Corte2 for x in C2]
plt.plot(z, C1, z, C2)
plt.xlabel('Z')
plt.ylabel('Membresia')
plt.show()

Area = np.array([C1, C2]).max(axis=0)
plt.plot(z, Area)
plt.xlabel('Z')
plt.ylabel('Membresia')
plt.show()

salida=fuzz.centroid(z, Area)
