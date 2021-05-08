import numpy as np
import matplotlib.pyplot as mpl

x = range(-15, 15)


def a(x):
    return 1 / (1 + ((x + 5) / 7.5) ** 4)


def b(x):
    return 1 / (1 + ((x - 5) / 5) ** 2)


A = np.array(list(map(a, x)))
B = np.array(list(map(b, x)))


# T-Norma Hamacher
def Hamacher(r):
    return (A * B) / (r + (1 - r) * (A + B - (A * B)))


# T-Norma
def Schw4(p):
    return (A * B) / (A ** p + B ** p - (A ** p) * (B ** p)) ** (1 / p)


# T-Norma
def Schw3(p):
    return np.exp(-((np.abs(np.log(A)) ** p) + (np.abs(np.log(B)) ** p)) ** (1 / p))


Hama1 = Hamacher(1.5)
Hama2 = Hamacher(1.0)
Hama3 = Hamacher(0.5)
mpl.figure(1)
mpl.plot(x, Hama1)
mpl.plot(x, Hama2)
mpl.plot(x, Hama3)
mpl.legend(['0.5', '1.0', '1.5'])
mpl.title("T-Norma Hamacher")
mpl.show()
Schw41 = Schw4(0.5)
Schw42 = Schw4(1.0)
Schw43 = Schw4(1.5)
mpl.figure(2)
mpl.plot(x, Schw41)
mpl.plot(x, Schw42)
mpl.plot(x, Schw43)
mpl.legend(['0.5', '1.0', '1.5'])
mpl.title("T-Norma Schw4")
mpl.show()
Schw31 = Schw3(0.5)
Schw32 = Schw3(1.0)
Schw33 = Schw3(1.5)
mpl.figure(3)
mpl.plot(x, Schw31)
mpl.plot(x, Schw32)
mpl.plot(x, Schw33)
mpl.legend(['0.5', '1.0', '1.5'])
mpl.title("T-Norma Schw3")
mpl.show()


# S-Norma Hamacher
def SHamacher(r):
    return (A + B + (r - 2) * (A * B)) / (r + (r - 1) * (A * B))


# S-Norma
def SSchw4(p):
    return 1 - (((1 - A) * (1 - B)) / (((1 - A) ** p) + ((1 - B) ** p) - ((1 - A) ** p) * ((1 - B) ** p)) ** (1 / p))


# S-Norma
def SSchw3(p):
    return 1 - (np.exp(-((np.abs(np.log(1 - A)) ** p) + (np.abs(np.log(1 - B)) ** p)) ** (1 / p)))


SHama1 = SHamacher(0.5)
SHama2 = SHamacher(1.0)
SHama3 = SHamacher(1.5)
mpl.figure(4)
mpl.plot(x, SHama1)
mpl.plot(x, SHama2)
mpl.plot(x, SHama3)
mpl.legend(['0.5', '1.0', '1.5'])
mpl.title("S-Norma Hamacher")
mpl.show()
SSchw41 = SSchw4(0.5)
SSchw42 = SSchw4(1.0)
SSchw43 = SSchw4(1.5)
mpl.figure(5)
mpl.plot(x, SSchw41)
mpl.plot(x, SSchw42)
mpl.plot(x, SSchw43)
mpl.legend(['0.5', '1.0', '1.5'])
mpl.title("S-Norma Schw4")
mpl.show()
SSchw31 = SSchw3(0.5)
SSchw32 = SSchw3(1.0)
SSchw33 = SSchw3(1.5)
mpl.figure(6)
mpl.plot(x, SSchw31)
mpl.plot(x, SSchw32)
mpl.plot(x, SSchw33)
mpl.legend(['0.5', '1.0', '1.5'])
mpl.title("S-Norma Schw3")
mpl.show()
