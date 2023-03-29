import math
import matplotlib.pyplot as plt
import numpy as np

Dt = 0.001  # w sekundach
l = 1  # w metrach
g = -10  # w metrach na sekunde
m = 1  # w kg

tp = 0
alfa = math.radians(45)
omega = 0
eps = g/l * math.sin(alfa)

Da = omega * Dt
Dw = eps * Dt
x = l * math.cos(alfa - math.radians(90))
y = l * math.sin(alfa - math.radians(90))
h = y + l
V = l * omega

Ep = math.fabs(m * g * h)
Ek = math.pow((m * V), 2)/2
Ec = Ep + Ek

EpList = []
EkList = []
EcList = []
OmegaList = []
AlfaList = []
EpList.append(Ep)
EkList.append(Ek)
EcList.append(Ec)
OmegaList.append(omega)
AlfaList.append(alfa)

print("t  alfa  omega  eps  Da  Dw  x  y  h  V  Ep  Ek  Ec")
while tp < 3:
    print(str(tp) + ' ' + str(alfa) + ' ' + str(omega) + ' ' + str(eps) + ' ' + str(Da) + ' ' + str(Dw) + ' ' + str(x) + ' ' + str(y) + ' ' + str(h) + ' ' + str(V) + ' ' + str(Ep) + ' ' + str(Ek) + ' ' + str(Ec))
    alfa += Da
    omega += Dw
    eps = g / l * math.sin(alfa)
    Da = omega * Dt
    Dw = eps * Dt
    x = l * math.cos(alfa - math.radians(90))
    y = l * math.sin(alfa - math.radians(90))
    h = y + l
    V = l * omega
    Ep = math.fabs(m * g * h)
    Ek = math.pow((m * V), 2)/2
    Ec = Ep + Ek
    tp += Dt
    EpList.append(Ep)
    EkList.append(Ek)
    EcList.append(Ec)
    OmegaList.append(omega)
    AlfaList.append(alfa)

TList = np.arange(0, len(EpList)*0.001, 0.001)
plt.plot(TList, EpList)
plt.plot(TList, EkList)
plt.plot(TList, EcList)

# plt.plot(AlfaList, OmegaList)

plt.show()
