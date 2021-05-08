import numpy as np
import matplotlib.pyplot as mpl

Mt = np.array([0, 0.3, 0.7, 0.8, 0.9, 1])
Mr = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])
print("T-norma")
Min = np.array([Mt, Mr]).min(axis=0)
print("Minimo", Min)
ProdA = Mt * Mr
print("Producto algebraico", ProdA)
ProF = np.array([Mt + Mr - 1, [0, 0, 0, 0, 0, 0]]).max(axis=0)
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
SumaFrontera = np.array([Mt + Mr, [1, 1, 1, 1, 1, 1]]).min(axis=0)
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
x = range(0, 6)
mpl.figure()
mpl.plot(x, Min, x, ProdA, x, ProF, x, ProductoD())
mpl.legend(["Min", "Pa", "Pf", "Pd"])
mpl.figure()
mpl.plot(x, Max, x, SumaAlgebraica, x, SumaFrontera, x, SumaD())
mpl.legend(["Max", "Sa", "Sf", "Sd"])
mpl.show()
