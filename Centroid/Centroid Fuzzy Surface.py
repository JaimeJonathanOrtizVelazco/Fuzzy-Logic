import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

Trapezoid = lambda a, b, c, d, X: [
    (x - a) / (b - a) if a < x <= b else 1 if b < x <= c else (d - x) / (d - c) if c < x <= d else 0 for x in
    X]  # Declaracion de la funcion trapecio
x = range(0, 360)
TrapezoidGen1 = Trapezoid(0, 0, 20, 60, x)  # Definicion del conjunto A1
TrapezoidGen2 = Trapezoid(30, 70, 110, 150, x)  # Definicion del conjunto A2
TrapezoidGen3 = Trapezoid(120, 160, 200, 240, x)  # Definicion del conjunto A3
TrapezoidGen4 = Trapezoid(210, 250, 290, 330, x)  # Definicion del conjunto A4
TrapezoidGen5 = Trapezoid(300, 340, 360, 360, x)  # Definicion del conjunto A5
TrapezoidGen1[0] = 1
plt.figure(1)
plt.plot(x, TrapezoidGen1, x, TrapezoidGen2, x, TrapezoidGen3, x, TrapezoidGen4, x,
         TrapezoidGen5)  # Ploteo del universo X
plt.show()

TrapezoidVel1 = Trapezoid(0, 0, 20, 60, x)  # Definicion del conjunto B1
TrapezoidVel2 = Trapezoid(30, 70, 110, 150, x)  # Definicion del conjunto B2
TrapezoidVel3 = Trapezoid(120, 160, 200, 240, x)  # Definicion del conjunto B3
TrapezoidVel4 = Trapezoid(210, 250, 290, 330, x)  # Definicion del conjunto B4
TrapezoidVel5 = Trapezoid(300, 340, 360, 360, x)  # Definicion del conjunto B5
TrapezoidVel1[0] = 1

plt.figure(2)
plt.plot(x, TrapezoidVel1, x, TrapezoidVel2, x, TrapezoidVel3, x, TrapezoidVel4, x,
         TrapezoidVel5)  # Ploteo del universo Y
plt.show()

xSal = range(0, 600)
TrapVelocidad1 = Trapezoid(0, 0, 100, 175, xSal)  # Definicion del conjunto C1
TrapVelocidad2 = Trapezoid(125, 200, 400, 475, xSal)  # Definicion del conjunto C2
TrapVelocidad3 = Trapezoid(425, 500, 600, 600, xSal)  # Definicion del conjunto C3
TrapVelocidad1[0] = 1
plt.figure(3)
plt.plot(xSal, TrapVelocidad1, xSal, TrapVelocidad2, xSal, TrapVelocidad3)  # Ploteo del universo Z1
plt.show()

xGiro = np.arange(0, 2, .01)
TrapGiro1 = Trapezoid(0, 0, 0.4, 1, xGiro)  # Definicion del conjunto D1
TrapGiro2 = Trapezoid(0.6, 0.9, 1.1, 1.4, xGiro)  # Definicion del conjunto D12
TrapGiro3 = Trapezoid(1, 1.6, 2, 2, xGiro)  # Definicion del conjunto D3
TrapGiro1[0] = 1

plt.figure(4)
plt.plot(xGiro, TrapGiro1, xGiro, TrapGiro2, xGiro, TrapGiro3)  # Ploteo del universo Z2
plt.show()
zVelocidad = np.zeros(
    [len(x), len(x)])  # Declaracion del arreglo que contendra todos los valores del la superficie de control para Z1
zGiro = np.zeros(
    [len(x), len(x)])  # Declaracion del arreglo que contendra todos los valores del la superficie de control para Z2

for xindex, X in enumerate(x):
    for yindex, Y in enumerate(x):  # For anidado para pasar por todas las muestras de los universos X y Y
        MFGenerador = [TrapezoidGen1[xindex], TrapezoidGen2[xindex], TrapezoidGen3[xindex], TrapezoidGen4[xindex],
                       TrapezoidGen5[xindex]]
        MFVeleta = [TrapezoidVel1[yindex], TrapezoidVel2[yindex], TrapezoidVel3[yindex], TrapezoidVel4[yindex],
                    TrapezoidVel5[yindex]]
        R1 = min(MFGenerador[0],
                 MFVeleta[0])  # Definicion de las reglas 25 para lo relacion de los universos y la salida
        R2 = min(MFGenerador[1], MFVeleta[0])
        R3 = min(MFGenerador[2], MFVeleta[0])
        R4 = min(MFGenerador[3], MFVeleta[0])
        R5 = min(MFGenerador[4], MFVeleta[0])
        R6 = min(MFGenerador[0], MFVeleta[1])
        R7 = min(MFGenerador[1], MFVeleta[1])
        R8 = min(MFGenerador[2], MFVeleta[1])
        R9 = min(MFGenerador[3], MFVeleta[1])
        R10 = min(MFGenerador[4], MFVeleta[1])
        R11 = min(MFGenerador[0], MFVeleta[2])
        R12 = min(MFGenerador[1], MFVeleta[2])
        R13 = min(MFGenerador[2], MFVeleta[2])
        R14 = min(MFGenerador[3], MFVeleta[2])
        R15 = min(MFGenerador[4], MFVeleta[2])
        R16 = min(MFGenerador[0], MFVeleta[3])
        R17 = min(MFGenerador[1], MFVeleta[3])
        R18 = min(MFGenerador[2], MFVeleta[3])
        R19 = min(MFGenerador[3], MFVeleta[3])
        R20 = min(MFGenerador[4], MFVeleta[3])
        R21 = min(MFGenerador[0], MFVeleta[4])
        R22 = min(MFGenerador[1], MFVeleta[4])
        R23 = min(MFGenerador[2], MFVeleta[4])
        R24 = min(MFGenerador[3], MFVeleta[4])
        R25 = min(MFGenerador[4], MFVeleta[4])
        CorteVelocidad1 = max(R1, R5, R7, R13, R19, R21, R25)  # Valor maximo de corte para los conjuntos de salida
        CorteVelocidad2 = max(R2, R4, R6, R8, R10, R12, R14, R16, R18, R20, R22, R24)
        CorteVelocidad3 = max(R3, R9, R11, R15, R17, R23)
        CorteSendio1 = max(R2, R3, R8, R14, R15, R16, R17, R20, R22)
        CorteSendio2 = max(R1, R5, R7, R13, R19, R21, R25)
        CorteSendio3 = max(R4, R6, R9, R10, R11, R12, R18, R23, R24)
        CV1 = [x if x < CorteVelocidad1 else CorteVelocidad1 for x in
               TrapVelocidad1]  # Corte de los conjuntos de salida
        CV2 = [x if x < CorteVelocidad2 else CorteVelocidad2 for x in TrapVelocidad2]
        CV3 = [x if x < CorteVelocidad3 else CorteVelocidad3 for x in TrapVelocidad3]
        CS1 = [x if x < CorteSendio1 else CorteSendio1 for x in TrapGiro1]
        CS2 = [x if x < CorteSendio2 else CorteSendio2 for x in TrapGiro2]
        CS3 = [x if x < CorteSendio3 else CorteSendio3 for x in TrapGiro3]
        AreaVelocidad = np.array([CV1, CV2, CV3]).max(axis=0)  # Maxima area del conjunto de salida para la velocidad
        AreaGiro = np.array([CS1, CS2, CS3]).max(
            axis=0)  # Maxima area del conjunto de salida para la direccion del giro
        zVelocidad[xindex, yindex] = fuzz.centroid(xSal,
                                                   AreaVelocidad)  # Obtencion del centroide para el rango Z1 en el sistema difuso
        zGiro[xindex, yindex] = fuzz.centroid(xGiro,
                                              AreaGiro)  # Obtencion del centroide para el rango Z2 en el sistema difuso
plotx = np.tile(x, (len(x), 1))  # Repeticion de los rangos en X para ploteo en 3D
ploty = np.tile(x, (len(x), 1)).T  # Repeticion de los rangos en y para ploteo en 3D
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, zVelocidad,
                cmap='viridis')  # Ploteo de la superficie de control para la velocidad de giro
ax.grid(True)
plt.show()
fig2 = plt.figure()
ax2 = plt.axes(projection='3d')
ax2.plot_surface(plotx, ploty, zGiro, cmap='viridis')  # Ploteo de la superficie de control para el sentido de giro
ax2.grid(True)
plt.show()
