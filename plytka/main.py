import numpy as np
import matplotlib.pyplot as plt

# wymiar plytki
x_min, x_max = 0, 15
y_min, y_max = 0, 20

n = 40

# dlugosc miedzy wezlami
dx = (x_max - x_min) / n
dy = (y_max - y_min) / n

x = np.linspace(x_min, x_max, n + 1)
y = np.linspace(y_min, y_max, n + 1)

A = np.zeros(((n + 1) * (n + 1), (n + 1) * (n + 1)))
b = np.zeros((n + 1) * (n + 1))

for i in range(1, n):
    for j in range(1, n):
        idx = i * (n + 1) + j

        A[idx, idx] = -4

        A[idx, idx - 1] = 1
        A[idx, idx + 1] = 1

        A[idx, idx - (n + 1)] = 1
        A[idx, idx + (n + 1)] = 1

        b[idx] = 0

for j in range(n + 1):
    # gora
    idx = j
    A[idx, idx] = 1
    b[idx] = 200

    # dol
    idx = n * (n + 1) + j
    A[idx, idx] = 1
    b[idx] = 150

for i in range(1, n):
    # lewa
    idx = i * (n + 1)
    A[idx, idx] = 1
    b[idx] = 100

    # prawa
    idx = i * (n + 1) + n
    A[idx, idx] = 1
    b[idx] = 50

T = np.linalg.solve(A, b)
T = T.reshape((n + 1, n + 1))

plt.imshow(T, cmap='hot')
plt.colorbar()
plt.title("Rozklad temperatury na plytce")
plt.show()
