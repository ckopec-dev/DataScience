#
#
#
# RZ function visualized
# This version is incorrect. The y-axis is inverted and axes are wrong.
#
#
#

import Helper as help
import matplotlib.pyplot as plt
import math
import numpy as np
from mpmath import *
    
c1 = help.ComplexMatrix(-10, 10, -5, 35, pixel_density=16)
print("c1: " + str(c1.shape)) # 640,320

c2 = np.array(c1, copy=False, dtype=bool)
print("c2: " + str(c2.shape))

for idx, x in np.ndenumerate(c1):
    z = zeta(x)
    pure = help.IsPure(z)
    c2[idx] = pure
    print(idx, x, z, pure)

plt.imshow(c2, cmap="binary")
plt.gca().set_aspect("equal")
#plt.xlim([-10,10])
#plt.ylim([-5,35])
plt.tight_layout()

plt.savefig("Experiment15.png")
plt.show()


