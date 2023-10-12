import matplotlib.pyplot as plt

# 2d line plot
plt.plot([1,2,3],[7,8,9])
plt.title('Basic2DPlot')
plt.xlabel('x label')
plt.ylabel('y label')

plt.savefig("Basic2DPlot.png")
plt.show()