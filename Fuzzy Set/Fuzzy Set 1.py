import numpy as np
import matplotlib.pyplot as plt

x = range(0, 10)


def A(value):
    return value / (value + 2)


def B(value):
    return 2 ** -value


def C(value):
    return 1 / (1 + 10 * (value - 2) ** 2)


plt.figure(1)
a = np.array(list(map(A, x)))
a = a / a.max(axis=0)
plt.subplot(311)
plt.plot(x, a)
plt.title("A")
b = np.array(list(map(B, x)))
b = b / b.max(axis=0)
plt.subplot(312)
plt.plot(x, b)
plt.title("B")
c = np.array(list(map(C, x)))
c = c / c.max(axis=0)
plt.subplot(313)
plt.plot(x, c)
plt.title("C")

plt.figure(2)
Acon = 1 - a
plt.subplot(311)
plt.plot(x, Acon)
plt.title("A Conjunto")
Bcon = 1 - b
plt.subplot(312)
plt.plot(x, Bcon)
plt.title("B Conjunto")
Ccon = 1 - c
plt.subplot(313)
plt.plot(x, Ccon)
plt.title("C Conjunto")

plt.figure(3)
AuB = np.array([a, b]).max(axis=0)
plt.subplot(311)
plt.plot(x, AuB)
plt.title("AuB")
AuC = np.array([a, c]).max(axis=0)
plt.subplot(312)
plt.plot(x, AuC)
plt.title("AuC")
BuC = np.array([b, c]).max(axis=0)
plt.subplot(313)
plt.plot(x, BuC)
plt.title("BuC")

plt.figure(4)
AnB = np.array([a, b]).min(axis=0)
plt.subplot(311)
plt.plot(x, AnB)
plt.title("AnB")
AnC = np.array([a, c]).min(axis=0)
plt.subplot(312)
plt.plot(x, AnC)
plt.title("AnC")
BnC = np.array([b, c]).min(axis=0)
plt.subplot(313)
plt.plot(x, BnC)
plt.title("BnC")

plt.figure(5)
AnCconCon = 1 - np.array([a, Ccon]).min(axis=0)
plt.subplot(311)
plt.plot(x, AnCconCon)
plt.title("An_C Conjunto")
BconCCon = 1 - np.array([Bcon, c]).min(axis=0)
plt.subplot(312)
plt.plot(x, BconCCon)
plt.title("_BC Conjunto")
AuCcon = 1 - AuC
plt.subplot(313)
plt.plot(x, AuCcon)
plt.title("AuC Conjunto")

plt.show()
