#
#
#
# Plot with 2 lines demo
#
#
#

import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x, y, label='First line')
plt.plot(x2,y2, label='Second line')

plt.xlabel('This is the x axis')
plt.ylabel('This is the y axis')

plt.title('This is the title')

plt.legend()

plt.savefig("Experiment20.png")
plt.show()
