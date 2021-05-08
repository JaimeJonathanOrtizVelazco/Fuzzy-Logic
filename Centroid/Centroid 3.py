import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

Gaus = lambda b, sigma, X: [np.exp(-0.5 * ((x - b) / sigma) ** 2) for x in X]
GBel = lambda a, b, c, X: [1 / (1 + abs((x - c) / a) ** (2 * b)) for x in X]

climaRange = range(0, 40)
b1 = 0
b2 = 20
b3 = 40
sigmaClima = 10
Clima1 = Gaus(0, sigmaClima, climaRange)
Clima2 = GBel(8, 3, 20, climaRange)
Clima3 = Gaus(40, sigmaClima, climaRange)
plt.figure()
plt.plot(climaRange, Clima1, climaRange, Clima2, climaRange, Clima3)

aguaDepositRange = range(0, 1000)
AguaDeposito1 = GBel(90, 3, 0, aguaDepositRange)
AguaDeposito2 = GBel(90, 3, 250, aguaDepositRange)
AguaDeposito3 = GBel(90, 3, 500, aguaDepositRange)
AguaDeposito4 = GBel(90, 3, 750, aguaDepositRange)
AguaDeposito5 = GBel(90, 3, 1000, aguaDepositRange)
plt.figure()
plt.plot(aguaDepositRange, AguaDeposito1, aguaDepositRange, AguaDeposito2, aguaDepositRange, AguaDeposito3,
         aguaDepositRange, AguaDeposito4, aguaDepositRange, AguaDeposito5)

humedadRange = np.arange(0, 3, 0.1)
HumedadTierra1 = GBel(0.6, 3, 0, humedadRange)
HumedadTierra2 = GBel(0.6, 3, 1.5, humedadRange)
HumedadTierra3 = GBel(0.6, 3, 3, humedadRange)
plt.figure()
plt.plot(humedadRange, HumedadTierra1, humedadRange, HumedadTierra2, humedadRange, HumedadTierra3)

aguaSalidaRange = range(0, 1000)
AguaSalida1 = GBel(150, 3, 0, aguaSalidaRange)
AguaSalida2 = GBel(150, 3, 350, aguaSalidaRange)
AguaSalida3 = GBel(150, 3, 650, aguaSalidaRange)
AguaSalida4 = GBel(150, 3, 1000, aguaSalidaRange)
plt.figure()
plt.plot(aguaSalidaRange, AguaSalida1, aguaSalidaRange, AguaSalida2, aguaSalidaRange, AguaSalida3, aguaSalidaRange,
         AguaSalida4)

zAgua_salidaClima_Agua = np.zeros([len(climaRange), len(aguaDepositRange)])
zAgua_salidaClima_Humedad = np.zeros([len(climaRange), len(humedadRange)])
zAgua_salidaHumedad_Agua = np.zeros([len(humedadRange), len(aguaDepositRange)])

for xindex, X in enumerate(climaRange):
    for yindex, Y in enumerate(aguaDepositRange):
        for zindex, Z in enumerate(humedadRange):
            MFClima = [Clima1[xindex], Clima2[xindex], Clima3[xindex]]
            MFAguaDeposito = [AguaDeposito1[yindex], AguaDeposito2[yindex], AguaDeposito3[yindex],
                              AguaDeposito4[yindex],
                              AguaDeposito5[yindex]]
            MFHumedadTierra = [HumedadTierra1[zindex], HumedadTierra2[zindex], HumedadTierra3[zindex]]
            R1 = min(MFClima[0], MFAguaDeposito[0], MFHumedadTierra[0])
            R2 = min(MFClima[0], MFAguaDeposito[0], MFHumedadTierra[1])
            R3 = min(MFClima[0], MFAguaDeposito[0], MFHumedadTierra[2])
            R4 = min(MFClima[0], MFAguaDeposito[1], MFHumedadTierra[0])
            R5 = min(MFClima[0], MFAguaDeposito[1], MFHumedadTierra[1])
            R6 = min(MFClima[0], MFAguaDeposito[1], MFHumedadTierra[2])
            R7 = min(MFClima[0], MFAguaDeposito[2], MFHumedadTierra[0])
            R8 = min(MFClima[0], MFAguaDeposito[2], MFHumedadTierra[1])
            R9 = min(MFClima[0], MFAguaDeposito[2], MFHumedadTierra[2])
            R10 = min(MFClima[0], MFAguaDeposito[3], MFHumedadTierra[0])
            R11 = min(MFClima[0], MFAguaDeposito[3], MFHumedadTierra[1])
            R12 = min(MFClima[0], MFAguaDeposito[3], MFHumedadTierra[2])
            R13 = min(MFClima[0], MFAguaDeposito[4], MFHumedadTierra[0])
            R14 = min(MFClima[0], MFAguaDeposito[4], MFHumedadTierra[1])
            R15 = min(MFClima[0], MFAguaDeposito[4], MFHumedadTierra[2])
            R16 = min(MFClima[1], MFAguaDeposito[0], MFHumedadTierra[0])
            R17 = min(MFClima[1], MFAguaDeposito[0], MFHumedadTierra[1])
            R18 = min(MFClima[1], MFAguaDeposito[0], MFHumedadTierra[2])
            R19 = min(MFClima[1], MFAguaDeposito[1], MFHumedadTierra[0])
            R20 = min(MFClima[1], MFAguaDeposito[1], MFHumedadTierra[1])
            R21 = min(MFClima[1], MFAguaDeposito[1], MFHumedadTierra[2])
            R22 = min(MFClima[1], MFAguaDeposito[2], MFHumedadTierra[0])
            R23 = min(MFClima[1], MFAguaDeposito[2], MFHumedadTierra[1])
            R24 = min(MFClima[1], MFAguaDeposito[2], MFHumedadTierra[2])
            R25 = min(MFClima[1], MFAguaDeposito[3], MFHumedadTierra[0])
            R26 = min(MFClima[1], MFAguaDeposito[3], MFHumedadTierra[1])
            R27 = min(MFClima[1], MFAguaDeposito[3], MFHumedadTierra[2])
            R28 = min(MFClima[1], MFAguaDeposito[4], MFHumedadTierra[0])
            R29 = min(MFClima[1], MFAguaDeposito[4], MFHumedadTierra[1])
            R30 = min(MFClima[1], MFAguaDeposito[4], MFHumedadTierra[2])
            R31 = min(MFClima[2], MFAguaDeposito[0], MFHumedadTierra[0])
            R32 = min(MFClima[2], MFAguaDeposito[0], MFHumedadTierra[1])
            R33 = min(MFClima[2], MFAguaDeposito[0], MFHumedadTierra[2])
            R34 = min(MFClima[2], MFAguaDeposito[1], MFHumedadTierra[0])
            R35 = min(MFClima[2], MFAguaDeposito[1], MFHumedadTierra[1])
            R36 = min(MFClima[2], MFAguaDeposito[1], MFHumedadTierra[2])
            R37 = min(MFClima[2], MFAguaDeposito[2], MFHumedadTierra[0])
            R38 = min(MFClima[2], MFAguaDeposito[2], MFHumedadTierra[1])
            R39 = min(MFClima[2], MFAguaDeposito[2], MFHumedadTierra[2])
            R40 = min(MFClima[2], MFAguaDeposito[3], MFHumedadTierra[0])
            R41 = min(MFClima[2], MFAguaDeposito[3], MFHumedadTierra[1])
            R42 = min(MFClima[2], MFAguaDeposito[3], MFHumedadTierra[2])
            R43 = min(MFClima[2], MFAguaDeposito[4], MFHumedadTierra[0])
            R44 = min(MFClima[2], MFAguaDeposito[4], MFHumedadTierra[1])
            R45 = min(MFClima[2], MFAguaDeposito[4], MFHumedadTierra[2])
            CorteAguaSalida1 = max(R1, R2, R3, R5, R6, R8, R9, R11, R12, R14, R15, R16, R17, R18, R20, R21, R24, R27,
                                   R30, R31, R32, R33, R36)
            CorteAguaSalida2 = max(R4, R7, R10, R13, R19, R23, R35, R39, R42, R45)
            CorteAguaSalida3 = max(R22, R26, R29, R38, R41)
            CorteAguaSalida4 = max(R25, R28, R34, R37, R40, R43, R44)
            C1 = [x if x < CorteAguaSalida1 else CorteAguaSalida1 for x in
                  AguaSalida1]  # Corte de los conjuntos de salida
            C2 = [x if x < CorteAguaSalida2 else CorteAguaSalida2 for x in AguaSalida2]
            C3 = [x if x < CorteAguaSalida3 else CorteAguaSalida3 for x in AguaSalida3]
            C4 = [x if x < CorteAguaSalida3 else CorteAguaSalida3 for x in AguaSalida4]
            Area = np.array([C1, C2, C3, C4]).max(axis=0)
            zAgua_salidaClima_Agua[xindex, yindex] = fuzz.centroid(aguaSalidaRange, Area)
            zAgua_salidaClima_Humedad[xindex, zindex] = fuzz.centroid(aguaSalidaRange, Area)
            zAgua_salidaHumedad_Agua[zindex, yindex] = fuzz.centroid(aguaSalidaRange, Area)
plt.show()
