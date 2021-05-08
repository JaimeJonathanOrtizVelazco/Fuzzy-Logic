import numpy as np
import matplotlib.pyplot as mpl

x = range(-15, 15)


def A(x):
    return 1 / (1 + ((x + 5) / 7.5) ** 4)


def B(x):
    return 1 / (1 + ((x - 5) / 5) ** 2)


Mt = np.array(list(map(A, x)))
Mr = np.array(list(map(B, x)))
print("T-norma")
Min = np.array([Mt, Mr]).min(axis=0)
print("Minimo", Min)
ProdA = Mt * Mr
print("Producto algebraico", ProdA)
ProF = np.array([Mt + Mr - 1, np.zeros(len(x))]).max(axis=0)
print("Producto frontera", ProF)


def ProductoD():
    Pd = []
    for i, x in enumerate(Mr, start=0):
        if x == 1:
            Pd.append(Mt[i])
        elif Mt[i] == 1:
            Pd.append(x)
        else:
            Pd.append(0)
    return Pd


print("Producto Drastico", ProductoD())
print("S-norma")
Max = np.array([Mt, Mr]).max(axis=0)
print("Maximo", Max)
SumaAlgebraica = Mt + Mr - Mt * Mr
print("Suma algebraico", SumaAlgebraica)
SumaFrontera = np.array([Mt + Mr, [1 for x in range(-15, 15)]]).min(axis=0)
print("Suma frontera", SumaFrontera)


def SumaD():
    Smd = []
    for i, x in enumerate(Mr, start=0):
        if x == 0:
            Smd.append(Mt[i])
        elif Mt[i] == 0:
            Smd.append(x)
        else:
            Smd.append(1)
    return Smd


print("Suma drastica", SumaD())
mpl.figure(1)
mpl.plot(x, Min, x, ProdA, x, ProF, x, ProductoD())
mpl.legend(["Min", "Pa", "Pf", "Pd"])
mpl.figure(2)
mpl.plot(x, Max, x, SumaAlgebraica, x, SumaFrontera, x, SumaD())
mpl.legend(["Max", "Sa", "Sf", "Sd"])
mpl.show()
