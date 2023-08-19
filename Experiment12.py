#
#
#
# Log Integral test
#
#
#

from Helper import *
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.linspace(0, 1000.0, num=1000)
ypoints1 = np.empty(shape = xpoints.shape[0])
ypoints2 = np.empty(shape = xpoints.shape[0])

for i in range(0, ypoints1.shape[0]):
    ypoints1[i] = LogIntegral(xpoints[i], 10)
    ypoints2[i] = PiN(xpoints[i])

plt.plot(xpoints, ypoints1)
plt.plot(xpoints, ypoints2)

plt.show()
plt.savefig("Experiment12.png")
