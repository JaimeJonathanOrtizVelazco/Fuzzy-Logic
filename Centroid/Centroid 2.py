# Librerias
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

a1 = -0.3
c1 = 50
a2 = 0.3
c2 = 50
xrray = list(range(0, 100))  # Rango de las muestras
A1 = list(map(lambda x: 1 / (1 + np.exp(-a1 * (x - c1))), xrray))  # Definicion del conjunto A1
A2 = list(map(lambda x: 1 / (1 + np.exp(-a2 * (x - c2))), xrray))  # Definicion del conjunto A2
plt.plot(xrray, A1, xrray, A2)  # Plot del universo X
plt.xlabel('X')
plt.ylabel('Membresia')
plt.show()

b1 = 25
sigma1 = 20
b2 = 75
sigma2 = 20
yrray = xrray
B1 = list(map(lambda y: np.exp(-0.5 * ((y - b1) / sigma1) ** 2), yrray))  # Definicion del conjunto B1
B2 = list(map(lambda y: np.exp(-0.5 * ((y - b2) / sigma2) ** 2), yrray))  # Definicion del conjunto B2
plt.plot(yrray, B1, yrray, B2)  # Plot del universo Y
plt.xlabel('Y')
plt.ylabel('Membresia')
plt.show()

sa1 = -0.3
sc1 = 50
sc2 = 75
ssigma2 = 20
z = xrray
C1 = list(map(lambda z: 1 / (1 + np.exp(-sa1 * (z - sc1))), z))  # Definicion del conjunto C1
C2 = list(map(lambda z: np.exp(-0.5 * ((z - sc2) / ssigma2) ** 2), z))  # Definicion del conjunto C2
plt.plot(z, C1, z, C2)  # Plot del universo Z
plt.xlabel('Z')
plt.ylabel('Membresia')
plt.show()

zr = np.zeros(
    [len(xrray), len(yrray)])  # Declaracion del arreglo que contendra todos los valores del la superficie de control

for xindex, X in enumerate(xrray):
    for yindex, Y in enumerate(yrray):  # For anidado para pasar por todas las muestras de los universos X y Y
        MFX = [A1[xindex], A2[xindex]]
        MFY = [B1[yindex], B2[yindex]]
        R1 = min(MFX[0], MFY[0])  # Definicion de las reglas para lo relacion de los universos y la salida
        R2 = min(MFX[0], MFY[1])
        R3 = min(MFX[1], MFY[0])
        R4 = min(MFX[1], MFY[1])
        Corte1 = max(R1, R2)  # Valor maximo de corte para los conjuntos de salida
        Corte2 = max(R3, R4)
        C12 = [x if x < Corte1 else Corte1 for x in C1]  # Corte de los conjuntos de salida
        C22 = [x if x < Corte2 else Corte2 for x in C2]
        Area = np.array([C12, C22]).max(axis=0)  # Maxima area del conjunto de salida
        zr[xindex, yindex] = fuzz.centroid(z, Area)  # Obtencion del centroide para el rango Z en el sistema difuso

plotx = np.tile(xrray, (len(xrray), 1))  # Repeticion de los rangos en X para ploteo en 3D
ploty = np.tile(yrray, (len(yrray), 1)).T  # Repeticion de los rangos en Y para ploteo en 3D
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, zr, rstride=1, cstride=1, cmap='viridis',
                edgecolor='none')  # Ploteo de la superficie de control con los valores obtenidos en el for anidado zr
plt.show()
