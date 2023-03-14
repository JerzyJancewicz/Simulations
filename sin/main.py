import math
import numpy as np
import matplotlib.pyplot as plt


def taylor(x, times):
    taylor_sin = x - ((x ** 3) / math.factorial(3))

    z = 5
    for a in range(0, times):
        if a % 2 == 0:
            taylor_sin = taylor_sin - ((x ** z) / math.factorial(z))
            print(taylor_sin)
        else:
            taylor_sin = taylor_sin + ((x ** z) / math.factorial(z))
            print(taylor_sin)
        z = z + 2

    return taylor_sin



measurement_error = 0
