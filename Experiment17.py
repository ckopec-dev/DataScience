#
#
#
# Mandelbrot set, again
# https://stackoverflow.com/questions/60467316/displaying-mandelbrot-set-in-python-using-matplotlib-pyplot-and-numpy
#
#
#

import pylab as plt
import numpy as np
# initial values 
loop = 50 # number of interations
div = 600 # divisions
# all possible values of c
c = np.linspace(-2,2,div)[:,np.newaxis] + 1j*np.linspace(-2,2,div)[np.newaxis,:] 
z = 0 
for n in range(0,loop):
      z = z**2 + c

plt.rcParams['figure.figsize'] = [12, 7.5] 
p = c[abs(z) < 2] # removing c values for which z has diverged 
plt.scatter(p.real, p.imag, color = "black" ) # plotting points
plt.xlabel("Real")
plt.ylabel("i (imaginary)")
plt.xlim(-2,2)
plt.ylim(-1.5,1.5)
plt.savefig("Experiment17.png")
plt.show()