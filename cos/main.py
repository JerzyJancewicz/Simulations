import numpy as np
import matplotlib.pyplot as plt

initialize_values = np.array([1, 1, 1])
A = 10
B = 25
C = 8 / 3

t_max = 80
dt = 0.03


def count_variables(array):
    x, y, z = array
    dx_dt = A * y - A * x
    dy_dt = -x * z + B * x - y
    dz_dt = x * y - C * z
    return np.array([dx_dt, dy_dt, dz_dt])


# Euler's method
def count_euler(initialize_values, t_max, dt):
    time = np.arange(0, t_max, dt)
    output_array = np.zeros((len(time), len(initialize_values)))
    output_array[0] = initialize_values

    for i in range(1, len(time)):
        output_array[i] = output_array[i - 1] + dt * count_variables(output_array[i - 1])
    return time, output_array


# Midpoint method
def count_midpoint(initialize_values, t_max, dt):
    time = np.arange(0, t_max, dt)
    output_array = np.zeros((len(time), len(initialize_values)))
    output_array[0] = initialize_values

    for i in range(1, len(time)):
        k1 = dt * count_variables(output_array[i - 1])
        k2 = dt * count_variables(output_array[i - 1] + 0.5 * k1)
        output_array[i] = output_array[i - 1] + k2
    return time, output_array


# RK4 method
def count_rk4(initialize_values, t_max, dt):
    time = np.arange(0, t_max, dt)
    output_array = np.zeros((len(time), len(initialize_values)))
    output_array[0] = initialize_values

    for i in range(1, len(time)):
        k1 = dt * count_variables(output_array[i - 1])
        k2 = dt * count_variables(0.5 * k1 + output_array[i - 1])
        k3 = dt * count_variables(0.5 * k2 + output_array[i - 1])
        k4 = dt * count_variables(k3 + output_array[i - 1])
        output_array[i] = output_array[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return time, output_array


# Euler
t_euler, output_euler = count_euler(initialize_values, t_max, dt)

plt.plot(output_euler[:, 0], output_euler[:, 2])
plt.xlabel("x")
plt.ylabel("z")
plt.title("Euler's Method")
plt.grid(True)
plt.show()

# Midpoint
t_midpoint, output_midpoint = count_midpoint(initialize_values, t_max, dt)

plt.plot(output_midpoint[:, 0], output_midpoint[:, 2])
plt.xlabel("x")
plt.ylabel("z")
plt.title("Midpoint Method")
plt.grid(True)
plt.show()

# RK4
t_rk4, output_rk4 = count_rk4(initialize_values, t_max, dt)

plt.plot(output_rk4[:, 0], output_rk4[:, 2])
plt.xlabel("x")
plt.ylabel("z")
plt.title("RK4 Method")
plt.grid(True)
plt.show()
