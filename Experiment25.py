import sys
import matplotlib.pyplot as plt
from sage.all import *
from pylab import * 

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def close(val):
	# To be used to determine if a number is arbitrarily close to zero.
	# Change the numbers below to adjust the tightness.
	if val >= -0.01 and val <= 0.01:
		return true
	else:
		return false

print("Calculating zeta values...")

xvals = []
yvals = []

granularity = 0.01

# Takes quite a while to execute...
for x in my_range(-10, 10, granularity):
	print ("Computing for real values of " + str(x) + "...")
	for y in my_range(-5, 35, granularity):
		z = zeta(x + y * i)
		zr = z.real()
		zi = z.imag()

		if close(zr) == true or close(zi) == true:
			xvals.append(x)
			yvals.append(y)
		  	#print str(x) + "," + str(y) + "," + str(zr) + "," + str(zi)

#print "xvals:"			
#print xvals
#print "yvals:"
#print yvals

print ("Writing image to file: Experiment25.jpg")
plt.plot(xvals, yvals, 'r.')
plt.axis([-10,10,-5,35])
#plt.savefig('Experiment25.png') 
plt.show()