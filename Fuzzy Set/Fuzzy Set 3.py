import matplotlib.pyplot as plt
import numpy as np


def a(x):
    if x <= 2 or x >= 6:
        return 0
    else:
        return 1


def b(x):
    if x <= 4 or x >= 8:
        return 0
    else:
        return 1


unit = range(0, 10)
plt.close()
plt.figure()
plt.title('Ambas funciones')
plt.step(unit, list(map(a, unit)), unit, list(map(b, unit)))

plt.figure()
union = np.array([list(map(a, unit)), list(map(b, unit))]).max(axis=0)
plt.title('Union AuB')
plt.step(unit, union)

plt.figure()
intersection = np.array([list(map(a, unit)), list(map(b, unit))]).min(axis=0)
plt.title('Interseccion AnB')
plt.step(unit, intersection)

plt.figure()
complement = 1 - np.array(list(map(a, unit)))
plt.title('Complemento')
plt.step(unit, complement)

plt.figure()
diff = [x if x >= 0 else 0 for x in np.array(list(map(a, unit))) - np.array(list(map(b, unit)))]
plt.title('Diferencia de A|B')
plt.step(unit, diff)
plt.show()
