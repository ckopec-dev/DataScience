#!/usr/bin/python3

# Riemann zeros: https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1

import math
import numpy as np
import matplotlib.pyplot as plt

zeros = np.loadtxt("RiemannZeros.txt")

# Plug the zeros into this function:

# f(x) = -cos(zero_1 * log(x)) - cos(zero_n * log(x))

xpoints = np.linspace(1, 16.0, num=10000)
ypoints = np.empty(shape = xpoints.shape[0])

for i in range(0, ypoints.shape[0]):
    print(i)
    if (i != 0):
        ypoints[i] = 0
        for j in range(0, 11):
            ypoints[i] = ypoints[i] - math.cos(zeros[j] * math.log(i))

plt.rcParams['figure.figsize'] = [12, 7.5] 
plt.plot(xpoints, ypoints)

plt.savefig("Experiment24.png")
plt.show()
