import math
import matplotlib.pyplot as plt

g = 10
Dt = 0.05
t = 0
r = 3
m = 1
h = 20
alfa = math.radians(45)
Ik = 2/5*m*r**2 # kula
Ik_sfery = 2/3*m*r**2 #sfera
acc = g*math.sin(alfa)/(1+Ik/(m*r**2))
eps = acc/r
d90 = math.radians(90)
length = 0 #pitagoras

Sx = 0
Sy = r
V = 0
DSx = V*Dt
Dv = acc*Dt
xr = Sx*math.cos(-alfa)-Sy*math.sin(-alfa)
yr = Sx*math.sin(-alfa) + Sy*math.cos(-alfa) + h
b = 0
w = 0
Db = w*Dt
Dw = eps * Dt
x = r * math.cos(d90 - b) + xr

Sx_List = []

def ik_object(object):
    if(object):
        return 2 / 5 * m * r ** 2
    else:
        return 2 / 3 * m * r ** 2


# def mid_point(t, Sx, Dsx, V, Dv, b, w, Db):
#     Sx += Dsx
#     V += Dv
#     Dsx = V * Dt
#     xr = Sx * math.cos(-alfa) - Sy*math.sin(-alfa)
#     yr = Sx * math.sin(-alfa) + Sy*math.cos(-alfa) + h
#     b += Db
#     w += Dw
#     Db = w * Dt
#     x = r * math.cos(d90-b) + xr
#     y = r * math.sin(d90 - b) + yr
#     Sx_List.append(Sx)

t_List = []
Vd = 0

while t < 3.35:
    V += Dv
    Sx += DSx
    acc = g * math.sin(alfa) / (1 + Ik / (m * r ** 2))
    Vd = acc * Dt / 2
    DSx = (V + Vd) * Dt
    Dv = acc * Dt
    xr = Sx * math.cos(-alfa) - Sy * math.sin(-alfa)
    yr = Sx * math.sin(-alfa) + Sy * math.cos(-alfa) + h
    b += Db
    w += Dw
    Db = w * Dt
    x = r * math.cos(d90 - b) + xr
    y = r * math.sin(d90 - b) + yr
    Sx_List.append(Sx)
    print("s")
    t_List.append(t)
    t += Dt
    print(Sx)


x = [0, 20]
y = [20, 0]


plt.plot(t_List, Sx_List)

plt.xlim(0, 10)
plt.ylim(0, 30)

plt.show()