# hw8pr1.py
# Lab 8
#
# Name:
#

# keep this import line...
from cs5png3 import *


#
# a test function...
#
def test_fun():
	""" algorithmic image-creation one pixel at a time...
		this is a test function: it should output
		an image named test.png in the same directory
	"""
	im = PNGImage(300,200)  # creates an image of width=300, height = 200

	# Nested loops!
	for r in range(200):  # loops over the rows with runner-variable r
		for c in range(300):  # loops over the cols with c
			if  c == r:   
				im.plotPoint( c, r, (255,0,0))
			#else:
			#	im.plotPoint( c, r, (255,0,0))
				
	im.saveFile()

#
# start your Lab 8 functions here:
#


def mult(c,n):
	"""Multiplies c by n using only addition (adds c to result n times)"""
	result = 0
	for i in range(n):
		result += c
	return result


def inMSet(c,n):
	"""Takes a complex number, c, and a number if iterations, n, and checks to see if c
	is in the Mandelbrot Set"""
	z = 0 + 0j

	for i in range(n):
		z = z**2+c

		if abs(z) > 2: 
			return False	
	return True
				

def weWantThisPixel(col, row):
	""" a function that returns True if we want
		 the pixel at col, row and False otherwise
	"""

	#Instead of only placing a mark when both are true, it will do it when either
	#are true. This means it will draw not only the nodes (dots) but also the horizontal
	#and vertical lines
	if col%10 == 0  or  row%10 == 0:
		return True
	else:
		return False


def scale(pix, pixMax, floatMin, floatMax):
	""" scale accepts
			pix, the CURRENT pixel column (or row)
			pixMax, the total # of pixel columns
			floatMin, the min floating-point value
			floatMax, the max floating-point value
		scale returns the floating-point value that
			corresponds to pix
	"""

	if pix == pixMax: return floatMax
	elif pix == 0: return floatMin
	else:
		pixFraction = float(pix)/float(pixMax)
		total = abs(floatMin) + abs(floatMax)
		floatFraction = (total*pixFraction)+(floatMin)
		return floatFraction


def mset():
	""" creates a 300x200 image of the Mandelbrot set
	"""
	width = 300
	height = 200
	image = PNGImage(width, height)
	NUMITER = 100  # of updates, from above
	XMIN = -2.0   # the smallest real coordinate value
	XMAX =  1.0   # the largest real coordinate value
	YMIN = -1.0   # the smallest imag coordinate value
	YMAX =  1.0   # the largest imag coordinate value

	# create a loop in order to draw some pixels
	
	for col in range(width):
		for row in range(height):
			# here is where you will need
			# to create the complex number, c!
			# Use scale twice:
			#   once to create the real part of c (x)
			x = scale(col, width, XMIN, XMAX)
			
			#   once to create the imag. part of c (y)
			y = scale(row, height, YMIN, YMAX)

			c = x + (y * 1j)
			# THEN, test if it's in the M. Set:

			if inMSet(c, NUMITER):
				image.plotPoint(col, row, (141,255,205))
			else:
				image.plotPoint(col,row, (83,55,71))

	# we looped through every image pixel; we now write the file
	image.saveFile()


mset()