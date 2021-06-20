from random import randint
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

fileNames = ['Botella-1', 'Botella-2', 'Botella-3', 'Botella-4', 'Botella-5', 'Botella-6', 'Botella-7', 'Botella-8',
             'Elevador 1', 'Elevador 2', 'Elevador 3', 'Elevador 4', 'Elevador 5', 'Elevador 6', 'Elevador 7',
             'Elevador 8', 'Agua 1', 'Agua 2', 'Agua 3', 'Agua 4', 'Agua 5', 'Agua 6', 'Agua 7','Agua 8']


def plotSignal(fs, data, title):
    l_audio = len(data.shape)
    if l_audio == 2:
        data = data.sum(axis=1) / 2
    L = len(data)
    Ts = 1 / fs
    t = np.linspace(0, L * Ts, L, endpoint=False)
    plt.figure()
    plt.plot(t, data)
    plt.title(title)
    plt.show()
    return data, L, Ts


def plotFFT(data, L, Ts, title):
    Y = abs(fft(data))[:L // 2]
    X = fftfreq(L, Ts)[:L // 2]
    plt.figure()
    plt.plot(X, Y)
    plt.ylabel('Magnitud')
    plt.xlabel('Frecuencia')
    plt.title(title)
    plt.show()
    return Y


def EntropiPoints(Y: np.array):
    EY = Y.var()
    EX = np.sum(Y * np.log2(Y))
    return EX, EY


entropies = []
for index, name in enumerate(fileNames):
    fs, data = wavfile.read(name + '.wav')
    data, L, Ts = plotSignal(fs, data, name)
    Y = np.array(plotFFT(data, L, Ts, name))
    EX, EY = EntropiPoints(Y)
    entropies.append([EX, EY])
entropies = np.array(entropies)

plt.figure()
plt.scatter(entropies[0:8].T[0], entropies[0:8].T[1])
plt.scatter(entropies[8:16].T[0], entropies[8:16].T[1])
plt.scatter(entropies[16:].T[0], entropies[16:].T[1])
plt.legend(
    ["Botella", "Elevador", "Agua"])
plt.ylabel('Varianza')
plt.xlabel('Entropia')
plt.show()

numclusters = 3
U0 = np.zeros(shape=(numclusters, entropies.shape[0]))
for index in range(0, entropies.shape[0]):
    randnum = randint(0, numclusters - 1)
    U0[randnum][index] = 1
U = np.zeros(shape=U0.shape)
d = np.zeros(shape=U0.shape)
m = 2
opr = np.zeros(shape=(numclusters, entropies.T.shape[0], entropies.T.shape[1]))
v = np.zeros(shape=(numclusters, entropies.T.shape[0]))
while True:
    for clus in range(numclusters):
        opr[clus] = (U0[clus] ** 2) * entropies.T
        v[clus] = np.sum(opr[clus], axis=1) / np.sum(U0[clus] ** 2)
    for xindex in range(entropies.shape[0]):
        for clus in range(numclusters):
            vald = 0
            for dims in range(entropies.T.shape[0]):
                vald += (entropies[xindex][dims] - v[clus][dims]) ** 2
            d[clus, xindex] = np.sqrt(vald)
    for xindex in range(U.shape[0]):
        for kindex in range(U.shape[1]):
            for jindex in range(d.shape[0]):
                U[xindex, kindex] += (d[xindex, kindex] / d[jindex, kindex]) ** (2 / (m - 1))
            U[xindex, kindex] = U[xindex, kindex] ** -1
    Val = np.sum((U0 - U) ** 2, axis=0)
    Val = np.sum(Val, axis=0)
    if Val >= 0.0005:
        U0 = U
        U = np.zeros(shape=U0.shape)
    else:
        break
U = np.around(U)
clusters = np.zeros(shape=(numclusters, entropies.T.shape[0], entropies.T.shape[1]))
clustersfre = []
for clus in range(numclusters):
    clusters[clus] = U[clus] * entropies.T
    notvalue = np.array(np.where(clusters[clus][0] == 0))
    clustersfre.append(np.array(np.delete(clusters[clus], notvalue, axis=1)))


def intersect(ls1: tuple, ls2: tuple):
    retunArra = []
    for valuel in ls1:
        if (ls2.__contains__(valuel)):
            retunArra.append(valuel)
    return len(retunArra)


def Efficiency(cluster):
    inter1 = intersect(tuple(cluster), tuple(entropies[0:8].tolist()))
    inter2 = intersect(tuple(cluster), tuple(entropies[8:16].tolist()))
    inter3 = intersect(tuple(cluster), tuple(entropies[16:].tolist()))
    if (inter1 > inter2 and inter1 > inter3):
        label = "Botella"
        porce = inter1 * 100 / 8 - (0 if len(cluster) < 8 else len(cluster) - 8) * 100 / 8
    elif (inter2 > inter3):
        label = "Elevador"
        porce = inter2 * 100 / 8 - (0 if len(cluster) < 8 else len(cluster) - 8) * 100 / 8
    else:
        label = "Agua"
        porce = inter3 * 100 / 8 - (0 if len(cluster) < 8 else len(cluster) - 8) * 100 / 8
    print("La eficiencia del cluster de la palabra '{}' es {}%".format(label, porce))
    return "Cluster {}".format(label)


clustercolors = ['r', 'b', 'g']
plt.figure()
for index in range(numclusters):
    label = Efficiency(clustersfre[index].T.tolist())
    plt.scatter(clustersfre[index][0], clustersfre[index][1], s=10, color=clustercolors[index])
    plt.scatter(v[index][0], v[index][1], s=40, color=clustercolors[index], marker="D", label=label)
plt.legend()
plt.title("Ponce CMeans")
plt.show()
fileNames = ['Botella-9', 'Botella-10', 'Elevador 9', 'Elevador 10', 'Agua 9', 'Agua 10']
entropiesTest = []
for index, name in enumerate(fileNames):
    fs, data = wavfile.read(name + '.wav')
    data, L, Ts = plotSignal(fs, data, name)
    Y = np.array(plotFFT(data, L, Ts, name))
    EX, EY = EntropiPoints(Y)
    entropiesTest.append([EX, EY])
    entropiesTest.append([EX, EY])
    entropiesTest.append([EX, EY])
    entropiesTest.append([EX, EY])
entropiesTest = np.array(entropiesTest)

clusters = np.zeros(shape=(numclusters, entropiesTest.T.shape[0], entropiesTest.T.shape[1]))
clustersfre = []
for clus in range(numclusters):
    clusters[clus] = U[clus] * entropiesTest.T
    notvalue = np.array(np.where(clusters[clus][0] == 0))
    clustersfre.append(np.array(np.delete(clusters[clus], notvalue, axis=1)))


def intersect(ls1: tuple, ls2: tuple):
    retunArra = []
    for valuel in ls1:
        if (ls2.__contains__(valuel)):
            retunArra.append(valuel)
    return len(retunArra)

clustercolors = ['r', 'b', 'g']
plt.figure()
for index in range(numclusters):
    plt.scatter(clustersfre[index][0], clustersfre[index][1], s=10, color=clustercolors[index])
    plt.scatter(v[index][0], v[index][1], s=40, color=clustercolors[index], marker="D")
plt.legend()
plt.title("Ponce CMeans")
plt.show()