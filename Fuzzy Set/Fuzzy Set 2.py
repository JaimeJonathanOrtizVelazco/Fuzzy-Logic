from FigureFunctions import Triangle, Trapezoid
import numpy as np
import matplotlib.pyplot as plt

triangle = Triangle(5, 8, 11)
trapezoid = Trapezoid(4, 6, 10, 12)
dim = range(0, 15)
A = list(map(triangle.print, dim))
B = list(map(trapezoid.print, dim))
CA = np.array([A]).T.repeat(len(B), axis=1)
CB = np.array([B]).repeat(len(A), axis=0)
tdDim = np.ones(CA.shape)
CAxCB = np.minimum(CA, CB)

plt.plot(dim, A)
plt.title('A')
plt.show()
plt.plot(dim, B)
plt.title('B')
plt.show()


def plotFigure(matrix, title):
    ca = plt.axes(projection='3d')
    ca.set_xlabel('x')
    ca.set_ylabel('y')
    ca.set_zlabel('M')
    ca.set_title(title)
    for index, pieceArray in enumerate(matrix):
        ca.plot3D([index for x in dim], dim, pieceArray)
    for index, pieceArray in enumerate(matrix.T):
        ca.plot3D(dim, [index for x in dim], pieceArray)
    plt.show()


plotFigure(CA, 'CA')
plotFigure(CB, 'CB')
plotFigure(CAxCB, 'CAxCB')
