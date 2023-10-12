from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax = plt.axes(projection='3d')

#3d line plot
zline = np.linspace(0, 10, 100)
xline = np.sin(zline)
yline = np.cos(zline)

ax.plot3D(xline, yline, zline, 'red')

plt.savefig("Basic3DPlot.png")
plt.show()