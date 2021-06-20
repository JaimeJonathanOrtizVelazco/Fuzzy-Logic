from math import dist

import numpy as np
from matplotlib import pyplot as plt
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import resize

original = io.imread('Im3-1.jpeg')  # Obtencion de imagen a analizar
original = resize(original, (480, 640), anti_aliasing=True)  # Redimesionamiento de la imagen
plt.figure(num=1)
plt.imshow(original)
plt.show()
img = rgb2gray(original)  # Conversion de la imagen a escala de grises
original = np.array(original)
plt.figure(num=2)
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
binarize = img < 0.63  # Ajuste de umbral para la imagen binarizada
plt.figure(num=3)
plt.imshow(binarize, cmap=plt.cm.gray)
plt.show()
x = []
for yindex in range(binarize.shape[0]):
    for xindex in range(binarize.shape[1]):
        if binarize[yindex, xindex]:
            x.append([xindex, yindex])
x = np.array(x)
C = np.arange(0, 480, 96)  # Enrejado para la altura de la imagen
F = np.arange(0, 640, 128)  # Enrejado para el largo de la imagen
alpha = .0095  # Definicion de las variable ajustadoras
beta = .0095
M = np.zeros(shape=(C.shape[0], F.shape[0]))  # Matriz principal
for yindex in range(C.shape[0]):
    for xindex in range(F.shape[0]):
        for zindex in range(x.shape[0]):
            d = np.sqrt(((x[zindex, 0] - F[xindex]) ** 2) + (
                    (x[zindex, 1] - C[yindex]) ** 2))  # distancia euclidiana de punto con los vertices de la reja
            M[yindex, xindex] += np.exp(-alpha * d)  # Primeras montañas con respecto a las posiciones del enrejado
plotx, ploty = np.meshgrid(F, C)  # Enrejado ajustado para ploteo
plt.figure(num=4)
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, M,
                cmap='viridis')  # Ploteo de la priomera montaña
ax.grid(True)
plt.title("Montaña 1")
plt.show()
k = 0  # Cantidad de clusteres
M2 = np.zeros(shape=M.shape)  # Matriz ajustable para montañas
MAc = []
pfc = list()
delta = [0]
c0 = list()
c = []
while delta[k] < 8:
    c.append(np.amax(M))
    for yindex in range(C.shape[0]):
        for xindex in range(F.shape[0]):
            if M[yindex, xindex] == c[k]:
                pfc.append((xindex, yindex))  # Posicion de la maxima montaña de M
                break
    for yindex in range(C.shape[0]):
        for xindex in range(F.shape[0]):
            g = 0
            for zindex in range(k + 1):
                dc = np.sqrt(((F[pfc[zindex][0]] - F[xindex]) ** 2) + (
                        (F[pfc[zindex][1]] - C[yindex]) ** 2))  # Distancia euclidiana
                g += np.exp(-beta * dc)
            val = M[yindex, xindex] - M[pfc[k][1], pfc[k][0]] * g
            if val >= 0:  # validacion para evitar numeros negativos
                M2[yindex, xindex] = val
            else:
                M2[yindex, xindex] = 0
    MAc.append(np.copy(M2))  # Agregado de nueva matriz con montaña unica
    delta.append(c[0] / np.amax(M2))  # Control de flujo de las figuras encontradas
    M = np.copy(M2)
    c0.append((F[pfc[k][0]], C[pfc[k][1]]))  # Ubicacion de los clusteres uniciales para Jang
    k += 1
c0 = set(c0)
c0 = np.array([list(x) for x in c0])
plt.figure(num=5)
plt.scatter(x.T[0], 479 - x.T[1], s=10)  # PLoteo de los objetos con sus posibles clusteres
plt.scatter(c0.T[0], 479 - c0.T[1], s=40, marker="D")
plt.grid(linewidth=1)
plt.show()
for xindex in range(len(c0) - 1):
    plt.figure(num=(6 + xindex))
    ax = plt.axes(projection='3d')
    ax.plot_surface(plotx, ploty, MAc[xindex], cmap='viridis')  # Ploteo de las montañas de los posibles objetos
    ax.grid(True)
    plt.title("Montaña {}".format(xindex + 2))
    plt.show()

U = np.zeros(shape=(c0.shape[0], x.shape[0]))
U0 = np.zeros(shape=(c0.shape[0], x.shape[0]))
# K-Means para clusteres iniciales
while True:
    for i in range(U.shape[0]):
        for j in range(U.shape[1]):
            flag = 0
            for k in range(c0.shape[0]):
                if i != k:
                    if dist(x[j], c0[i]) ** 2 <= dist(x[j], c0[k]) ** 2:
                        flag = 1
                    else:
                        flag = 0
                        break
            U[i, j] = flag
    G = np.zeros(U.shape[0])
    for uindex, uvalues in enumerate(U):
        G[uindex] = np.sum(uvalues)
    for uindex, uvalue in enumerate(U):
        c0[uindex] = np.sum(x.T * uvalue, axis=1) / G[uindex]
    if (np.array_equal(U0, U)):
        break
    else:
        U0 = U
        U = np.zeros(shape=(c0.shape[0], x.shape[0]))

objects = []
clusters = []
plt.figure()
for index in range(c0.shape[0]):
    clusters.append(x.T * U[index])  # Conjunto de datos con clusteres finales
    plt.scatter(clusters[index][0], 479 - clusters[index][1], s=10)
    objects.append("Objeto {}".format(index))
plt.legend(objects)
plt.scatter(c0.T[0], 479 - c0.T[1], s=40, marker="D")  # Clusteres finales por objeto
plt.title("Jang")
plt.show()
while True:
    option = int(input("Que objeto desea visualizar?"))
    if option > c0.shape[0] or option < 0:
        conti = input("Ingreso un valor incorrecto, desea volver a intenrarlo? S/N")
        if conti == "S":
            break
        else:
            continue
    im = np.zeros(shape=original.shape)
    for cord in clusters[option].T:
        im[int(cord[1]), int(cord[0])] = original[int(cord[1]), int(cord[0])]  # Imagen de objeto seleccionado unico
    plt.figure()
    plt.imshow(im)
    plt.show()
    conti = str(input("Desea volver a intenrarlo? S/N"))
    print(conti)
    if conti == 'N':
        break
