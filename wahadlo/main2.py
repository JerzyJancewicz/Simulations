import numpy as np
import matplotlib.pyplot as plt

g = 10
L = 1
m = 1

theta0 = np.radians(45)
omega0 = 0

t0 = 0
tmax = 6
dt = 0.001


def potential_energy(theta):
    return m*g*L*(1-np.cos(theta))


def kinetic_energy(omega):
    return 0.5*m*(L**2)*(omega**2)


def euler_step(theta, omega, dt):
    theta_new = theta + omega*dt
    omega_new = omega - (g/L)*np.sin(theta)*dt
    return theta_new, omega_new


def midpoint_step(theta, omega, dt):
    omega_half = omega - (g/L)*np.sin(theta)*0.5*dt
    theta_half = theta + omega_half*0.5*dt
    omega_new = omega - (g/L)*np.sin(theta_half)*dt
    theta_new = theta + omega_new*dt
    return theta_new, omega_new


def rk4_step(theta, omega, dt):
    k1 = omega*dt
    l1 = -(g/L)*np.sin(theta)*dt
    k2 = (omega+0.5*l1)*dt
    l2 = -(g/L)*np.sin(theta+0.5*k1)*dt
    k3 = (omega+0.5*l2)*dt
    l3 = -(g/L)*np.sin(theta+0.5*k2)*dt
    k4 = (omega+l3)*dt
    l4 = -(g/L)*np.sin(theta+k3)*dt
    theta_new = theta + (k1 + 2*k2 + 2*k3 + k4)/6
    omega_new = omega + (l1 + 2*l2 + 2*l3 + l4)/6
    return theta_new, omega_new


t = np.arange(t0, tmax+dt, dt)
theta_euler = np.zeros_like(t)
omega_euler = np.zeros_like(t)
theta_midpoint = np.zeros_like(t)
omega_midpoint = np.zeros_like(t)
theta_rk4 = np.zeros_like(t)
omega_rk4 = np.zeros_like(t)

theta_euler[0], omega_euler[0] = theta0, omega0
theta_midpoint[0], omega_midpoint[0] = theta0, omega0
theta_rk4[0], omega_rk4[0] = theta0, omega0

for i in range(1, len(t)):
    theta_euler[i], omega_euler[i] = euler_step(theta_euler[i-1], omega_euler[i-1], dt)
    theta_midpoint[i], omega_midpoint[i] = midpoint_step(theta_midpoint[i-1], omega_midpoint[i-1], dt)
    theta_rk4[i], omega_rk4[i] = rk4_step(theta_rk4[i-1], omega_rk4[i-1], dt)

    average_omega = (omega_euler[i] + omega_midpoint[i] + omega_rk4[i])/3
    average_theta = (theta_euler[i] + theta_midpoint[i] + theta_rk4[i])/3
    print(str(omega_euler[i]) + ' ' + str(omega_midpoint[i]) + ' ' + str(omega_rk4[i]) + ' ' + str(average_omega))
    print(str(theta_euler[i]) + ' ' + str(theta_midpoint[i]) + ' ' + str(theta_rk4[i]) + ' ' + str(average_theta))

E_potential_euler = potential_energy(theta_euler)
E_kinetic_euler = kinetic_energy(omega_euler)
E_total_euler = E_potential_euler + E_kinetic_euler

E_potential_midpoint = potential_energy(theta_midpoint)
E_kinetic_midpoint = kinetic_energy(omega_midpoint)
E_total_midpoint = E_potential_midpoint + E_kinetic_midpoint

E_potential_rk4 = potential_energy(theta_rk4)
E_kinetic_rk4 = kinetic_energy(omega_rk4)
E_total_rk4 = E_potential_rk4 + E_kinetic_rk4

# plt.plot(t, E_potential_euler)
# plt.plot(t, E_potential_midpoint)
# plt.plot(t, E_potential_rk4)
#
# plt.plot(t, E_kinetic_euler)
# plt.plot(t, E_kinetic_midpoint)
# plt.plot(t, E_kinetic_rk4)
#
# plt.plot(t, E_total_euler)
# plt.plot(t, E_total_midpoint)
# plt.plot(t, E_total_rk4)
#
# plt.plot(omega_euler, theta_euler)
# plt.plot(omega_midpoint,theta_midpoint)
# plt.plot(omega_rk4, theta_rk4)

plt.show()
