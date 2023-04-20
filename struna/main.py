import numpy as np
import matplotlib.pyplot as plt


def midpoint_method(position, V, a, Dt):
    V_second = V + 0.5 * a * Dt
    position_new = position + V_second * Dt
    a_new = count_a(position_new, dx)
    b_new = V_second + 0.5 * a_new * Dt
    return position_new, b_new, a_new


def count_a(position, dx):
    a = np.zeros_like(position)
    a[1:-1] = (position[:-2] - 2 * position[1:-1] + position[2:]) / dx ** 2
    return a


def count_energy(position, V, dx):
    Ep = np.sum((position[2:] - position[1:-1]) ** 2) / (2 * dx)
    Ek = np.sum(dx * V[1:-1] ** 2) / 2
    return Ek, Ep


L = np.pi
N = 10
dx = L / N
Dt = 0.01
T_all = 1000

position = np.sin(np.linspace(0, L, N + 1))
V = np.zeros_like(position)
a = count_a(position, dx)

Eps = []
Eks = []
Ecs = []

for t in range(T_all):
    position, V, a = midpoint_method(position, V, a, Dt)

    Ek, Ep = count_energy(position, V, dx)
    Ec = Ek + Ep

    Eks.append(Ek)
    Eps.append(Ep)
    Ecs.append(Ec)


plt.plot(Eks)
plt.plot(Eps)
plt.plot(Ecs)
plt.show()
