#
#
#
# Mandelbrot set: hi-res black + white
#
#
#

import Helper as help
import Mandelbrot as man
import matplotlib.pyplot as plt

c = help.ComplexMatrix(-2, 0.5, -1.5, 1.5, pixel_density=512) 
grid = man.is_stable(c, num_iterations=20)
plt.imshow(grid, cmap="binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()

plt.savefig("Experiment14.png")
plt.show()
