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
	if val >= -0.0001 and val <= 0.0001:
		return true
	else:
		return false

def create_data():
	print("Calculating zeta values...")

	xvals = []
	yvals = []

	granularity = 0.1 #0.01

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
				#print(str(x) + "," + str(y) + "," + str(zr) + "," + str(zi))

	# https://www.geeksforgeeks.org/python-append-to-a-file/
	fileX = open("Experiment25_XData.txt", "a")  # append mode
	fileX.write(str(xvals))
	fileX.close()

	fileY = open("Experiment25_YData.txt", "a")
	fileY.write(str(yvals))
	fileY.close()

def read_data():
	print("Loading zeta values...")

	xvals = []
	yvals = []

	fileX = open("Experiment25_XData.txt", "r")
	xvals = fileX.read()
	fileX.close()

	fileY = open("Experiment25_YData.txt", "r")
	yvals = fileY.read()
	fileY.close()
	
	return xvals, yvals

#create_data()
xvals, yvals = read_data()



# 			
#print "xvals:"			
#print xvals
#print "yvals:"
#print yvals

#print ("Writing image to file: Experiment25.jpg")
#plt.plot(xvals, yvals, 'r.')
#plt.axis([-10,10,-5,35])
#plt.savefig('Experiment25.png') 
#plt.show()