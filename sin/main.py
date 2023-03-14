import math
import numpy as np
import matplotlib.pyplot as plt


def taylor(x, times):
    taylor_sin = x - ((x ** 3) / math.factorial(3))

    z = 5
    for a in range(0, times):
        if a % 2 == 0:
            print(a)
            taylor_sin = taylor_sin - ((x ** z) / math.factorial(z))
            print(taylor_sin)
        else:
            taylor_sin = taylor_sin + ((x ** z) / math.factorial(z))
        z = z + 2

    return taylor_sin


def check_x(numb):

    if 0 < numb <= np.pi/2:
        return numb
    elif np.pi/2 < numb <= np.pi:
        return np.pi - numb
    elif np.pi < numb < 3/2*np.pi:
        return numb - np.pi
    elif 3/2*np.pi < numb <= 2*np.pi:
        return 2*np.pi - numb
    else:
        print(numb)
        return 0


x = np.arange(0, 2*np.pi, 0.1)   # start,stop,step

# Call check_x function on each element in x
y = taylor(np.array([check_x(xi) for xi in x]), 6)

# Convert output back to degrees
# y = np.degrees(y)

# Plot the result
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Taylor Series Approximation of Sin(x)')
plt.show()