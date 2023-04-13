import numpy as np
import matplotlib.pyplot as plt

G = 6.6743e-11
M_s = 1.989e30
M_z = 5.972e24
M_k = 7.342e22
R_zs = 1.5e11

# Inicjalizacja zmiennych

# Ziemia
r_zp = np.array([R_zs, 0, 0])
v_zp = np.array([0, np.sqrt(G * M_s / R_zs), 0])

# Księżyc
r_kp = np.array([R_zs + 384400000, 0, 0])
v_kp = np.array([0, np.sqrt(G * (M_s + M_k) / (R_zs + 384400000)), 0])

# Ksieżyc-Ziemia
r_kep = r_kp - r_zp
v_kep = v_kp - v_zp

dt = 3600
t_max = 10 * 365 * 24 * 3600


def f(r, v, M):
    return -G * M * r / np.linalg.norm(r) ** 3


# Midpoint
def midpoint(r, v, M, dt):
    v_first = f(r, v, M) * dt
    r_first = v * dt
    v_second = f(r + r_first / 2, v + v_first / 2, M) * dt
    r_second = (v + v_first / 2) * dt
    r_new = r + r_second
    v_new = v + v_second
    return r_new, v_new


t = 0
# Ziemia
r_z = r_zp
v_z = v_zp
r_z_list = []

# Księżyc
r_k = r_kp
v_k = v_kp
r_k_list = []

# # Ksieżyc-Ziemia
r_ke = r_kep
v_ke = v_kep
r_ke_list = []


while t <= t_max:
    r_z_list.append(r_z.copy())
    r_z, v_z = midpoint(r_z, v_z, M_s, dt)
    a_kz = f(r_k - r_z, v_k - v_z, M_z)
    r_k_list.append(r_k.copy())
    r_k, v_k = midpoint(r_k, v_k, M_s + M_z, dt)
    a_ks = f(r_k, v_k, M_s) + f(r_k - r_z, v_k - v_z, M_z)

    v_k += a_ks * dt
    r_k += v_k * dt

    r_k, v_k = midpoint(r_k, v_k, M_s + M_z, dt)

    t += dt

r_z_list = np.array(r_z_list)
r_k_list = np.array(r_k_list)

# r_z/k_list[:, 0] - Sx, r_z/k_list[:, 1] - Sy for Earth/Moon around Sun
plt.plot(r_z_list[:, 0], r_z_list[:, 1])
plt.plot(r_k_list[:, 0], r_k_list[:, 1])
plt.xlim(-2e11, 2e11)
plt.ylim(-2e11, 2e11)
plt.title('Orbita Ziemi i Księżyca wokół słońca')
plt.show()
