import math
import numpy as np


def taylor(x, times):
    taylor_sin = x - ((x ** 3) / math.factorial(3))
    tmp_taylor = taylor_sin
    z = 5
    for a in range(times):
        if a % 2 == 0:
            taylor_sin = tmp_taylor + ((x ** z) / math.factorial(z))
            #print(str(math.factorial(z)) + " " + str(z))
        else:
            taylor_sin = tmp_taylor - ((x ** z) / math.factorial(z))
            #print(str(math.factorial(z)) + " " + str(z))
        z = z + 2

    return taylor_sin


def check_x(numb):
    if 0 <= numb < math.pi/2:
        return numb
    elif math.pi/2 <= numb < math.pi:
        return math.pi - numb
    elif math.pi <= numb < 3/2*math.pi:
        return math.pi - numb
    elif 3/2*math.pi <= numb < 2*math.pi:
        return numb - 2*math.pi
    else:
        return 0


first = 0
for k in range(100):
    current = first + math.pi / 20

    taylor_numb = taylor(check_x(current), 50)
    np_sin = math.sin(current)
    measurement_error = np_sin - taylor_numb

    print(str(taylor_numb) + " " + str(np_sin) + " " + str(measurement_error))
    first = current


# x = np.arange(0, 2*np.pi, 0.1)   # start,stop,step
#
# # Call check_x function on each element in x
# y = taylor(np.array([check_x(xi) for xi in x]), 6)
#
# # Convert output back to degrees
# # y = np.degrees(y)
#
# # Plot the result
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Taylor Series Approximation of Sin(x)')
# plt.show()
