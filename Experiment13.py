#
#
#
# Mandelbrot set: basic scatter
# Ref: https://realpython.com/mandelbrot-set-python/
#
#
#

import Mandelbrot as man
import matplotlib.pyplot as plt

for n, z in enumerate(man.sequence(c=1)):
    print(f"z({n}) = {z}")
    if n >= 9:
        break

c = man.complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=21)
members = man.get_members(c, num_iterations=20)

plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()

plt.savefig("Experiment13.png")
plt.show()

