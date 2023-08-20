#
#
#
# Line plot demo
#
#
#

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

print(mpl.__version__)

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.savefig("Experiment18.png")
plt.show()

