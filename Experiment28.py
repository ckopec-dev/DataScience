import sys
import matplotlib.pyplot as plt
from sage.all import *
from pylab import * 
from Helper import *

def create_data():
	print("Calculating zeta values...")

	xvals = []
	yvals = []

	granularity = 0.01

	# Takes quite a while to execute...
	for x in MyRange(-10, 10, granularity):
		print ("Computing for real values of " + str(x) + "...")
		for y in MyRange(-5, 35, granularity):
			z = zeta(x + y * i)
			zr = z.real()
			zi = z.imag()
			
			if NearZero(zr) == true or NearZero(zi) == true:
				xvals.append(x)
				yvals.append(y)
				
	print("Created " + str(len(xvals)) + " xvals") #639
	print("Created " + str(len(yvals)) + " yvals") #639

	xvals = ["{}\n".format(i) for i in xvals]	
	with open(r"Experiment25_XData.txt", "w") as fx:
		fx.writelines(xvals)
		fx.close()
	
	yvals = ["{}\n".format(i) for i in yvals]	
	with open(r"Experiment25_YData.txt", "w") as fy:
		fy.writelines(yvals)
		fy.close()

def read_data():
	print("Loading zeta values...")

	xvals = []
	yvals = []

	with open("Experiment25_XData.txt") as f:
		xvals = [line.rstrip('\n') for line in f]

	with open("Experiment25_YData.txt") as f:
		yvals = [line.rstrip('\n') for line in f]

	print("Loaded " + str(len(xvals)) + " xvals")
	print("Loaded " + str(len(yvals)) + " yvals")
 	
	return xvals, yvals

def plot_data1(xvals, yvals):
	#print ("Writing image to file: Experiment25.jpg")
	plt.plot(xvals, yvals, 'r.')
	plt.axis([-10,10,-5,35])
	#plt.savefig('Experiment25.png') 
	plt.show()


create_data()
xvals, yvals = read_data()
plot_data1(xvals, yvals)

