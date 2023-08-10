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

print(LogIntegral(2, 10))

xpoints = np.linspace(0, 10.0, num=100)
ypoints = np.empty(shape = xpoints.shape[0])

print(math.log(0.10101010101010101))
for i in range(0, ypoints.shape[0]):
    ypoints[i] = LogIntegral(xpoints[i], 10)

plt.plot(xpoints, ypoints)
plt.show()

