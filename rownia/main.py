import math

import numpy as np
import matplotlib.pyplot as plt

#kula
mk = 1
rk = 3
ikK = 2 / 5 * mk * rk ** 2
wk = 0
gammaK = 0
bpK = 0
sxK = 0
vK = 0

#sfera
ms = 1
rs = 3
Iks = 2 / 3 * ms * rs ** 2
ws = 0
gammaS = 0
bpS = 0
sxS = 0
vS = 0

alfa = math.radians(45)
h = 20
g = 10

syS = 2
t = 0
dt = 0.05
maxT = 5
n = int(maxT / dt)

sxS_list = np.zeros(n)
syS_list = np.zeros(n)
gammaS_list = np.zeros(n)

sxK_list = np.zeros(n)
syK_list = np.zeros(n)
gammaK_list = np.zeros(n)
t_list = np.zeros(n)


def linear(ik, m, r, v, sx):
    acc = g * np.sin(alfa) / (1 + ik / (m * r ** 2))
    vd = acc * dt / 2
    dSx = (v + vd) * dt
    dV = acc * dt
    sx += dSx
    v += dV
    sy = r
    return sx, v, sy, acc


def rotational(r, w, acc, bp):
    eps = acc / r
    dw = eps * dt
    db = (w + dw / 2) * dt
    b = bp + db
    gamma = math.pi / 2 - b
    w += dw
    return gamma, w, db, b


for x in range(n):
    sxK, vK, syK, accK = linear(ikK, mk, rk, vK, sxK)
    gammaK, wk, dbk, bpK = rotational(rk, wk, accK, bpK)

    sxS, vS, syS, accS = linear(Iks, ms, rs, vS, sxS)
    gammaS, ws, dbS, bpS = rotational(rs, ws, accS, bpS)

    sxS_list[x] = sxS
    gammaS_list[x] = gammaS
    syS_list[x] = syS

    sxK_list[x] = sxK
    syK_list[x] = syK
    gammaK_list[x] = gammaK

    t_list[x] = t
    t += dt


# plt.plot(t_list, sxS_list)
# plt.plot(t_list, syS_list)
# plt.plot(t_list, gammaS_list)
#
# plt.plot(t_list, sxK_list)
# plt.plot(t_list, syK_list)
# plt.plot(t_list, gammaK_list)

plt.show()
