import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
import numpy as np


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


fs1, data1 = wavfile.read('Correr 1.wav')  # load the data
fs2, data2 = wavfile.read('Correr 2.wav')  # load the data
fs3, data3 = wavfile.read('Correr 3.wav')  # load the data
fs4, data4 = wavfile.read('Caminar 1.wav')  # load the data
fs5, data5 = wavfile.read('Caminar 2.wav')  # load the data
fs6, data6 = wavfile.read('Caminar 3.wav')  # load the data
fs7, data7 = wavfile.read('Saltar 1.wav')  # load the data
fs8, data8 = wavfile.read('Saltar 2.wav')  # load the data
fs9, data9 = wavfile.read('Saltar 3.wav')  # load the data
data1, L1, Ts1 = plotSignal(fs1, data1, 'Correr 1')
data2, L2, Ts2 = plotSignal(fs2, data2, 'Correr 2')
data3, L3, Ts3 = plotSignal(fs3, data3, 'Correr 3')
data4, L4, Ts4 = plotSignal(fs4, data4, 'Caminar 1')
data5, L5, Ts5 = plotSignal(fs5, data5, 'Caminar 2')
data6, L6, Ts6 = plotSignal(fs6, data6, 'Caminar 3')
data7, L7, Ts7 = plotSignal(fs7, data7, 'Saltar 1')
data8, L8, Ts8 = plotSignal(fs8, data8, 'Saltar 2')
data9, L9, Ts9 = plotSignal(fs9, data9, 'Saltar 3')


def plotFFT(data, L, Ts, title):
    Y = abs(fft(data))[:L // 2]
    X = fftfreq(L, Ts)[:L // 2]
    plt.figure()
    plt.plot(X, Y)
    plt.title(title)
    plt.show()
    return Y


Y1 = plotFFT(data1, L1, Ts1, 'Correr 1')
Y2 = plotFFT(data2, L2, Ts2, 'Correr 2')
Y3 = plotFFT(data3, L3, Ts3, 'Correr 3')
Y4 = plotFFT(data4, L4, Ts4, 'Caminar 1')
Y5 = plotFFT(data5, L5, Ts5, 'Caminar 2')
Y6 = plotFFT(data6, L6, Ts6, 'Caminar 3')
Y7 = plotFFT(data7, L7, Ts7, 'Saltar 1')
Y8 = plotFFT(data8, L8, Ts8, 'Saltar 2')
Y9 = plotFFT(data9, L9, Ts9, 'Saltar 3')
functionSecc = lambda Y: np.array([(x + 1) * xpos for x, xpos in enumerate(Y)])


def EntropiPoints(Y):
    RegY = functionSecc(Y)
    EY = np.sum(RegY * np.log2(RegY))
    EX = np.sum(Y * np.log2(Y))
    return EX, EY


EX1, EY1 = EntropiPoints(Y1)
EX2, EY2 = EntropiPoints(Y2)
EX3, EY3 = EntropiPoints(Y3)
EX4, EY4 = EntropiPoints(Y4)
EX5, EY5 = EntropiPoints(Y5)
EX6, EY6 = EntropiPoints(Y6)
EX7, EY7 = EntropiPoints(Y7)
EX8, EY8 = EntropiPoints(Y8)
EX9, EY9 = EntropiPoints(Y9)
plt.figure()
plt.scatter([EX1, EX2, EX3], [EY1, EY2, EY3])
plt.scatter([EX4, EX5, EX6], [EY4, EY5, EY6])
plt.scatter([EX7, EX8, EX9], [EY7, EY8, EY9])
plt.legend(
    ["Correr", "Caminar", "Saltar"])
plt.show()
