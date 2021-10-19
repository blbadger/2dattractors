# clifford_attractor.py

# A program to observe the behavior of the clifford map.
# Inspired by Vedran Sekara's post found here:
# https://vedransekara.github.io/2016/11/14/strange_attractors.html

# import third party libraries
import numpy as np 
import matplotlib.pyplot as plt 


def clifford_attractor(x, y, a=-2.1, b=-0.8, c=1.2, d=1.6):
	"""
	Returns the change in arguments x and y according to 
	the Clifford map equation. Kwargs a, b, c, and d are specified
	as constants.

	Args:
		x: float, current x coordinate
		y: float, current y coordinate
	kwargs:
		a, b, c, d: float, constant params

	Returns:
		x_next: float, next x coordinate
		y_next: float, next y coordinate

	"""

	x_next = np.sin(a*y) + c*np.cos(a*x) 
	y_next = np.sin(b*x) + d*np.cos(b*y)

	return x_next, y_next


def generate_map(iterations):
	"""
	Generate a map of the Clifford Attractor
	
	Args:
		iterations: int, number of steps plotted

	Returns:
		None (shows pyplot figure)
	
	"""

	# initialization
	x_arr, y_arr = [], []

	# starting point at (1, 1)
	x_arr.append(1), y_arr.append(1)


	for i in range(iterations-1):
		x_next, y_next = clifford_attractor(x_arr[-1], y_arr[-1])
		x_arr.append(x_next)
		y_arr.append(y_next)

	# make and display figure.
	plt.style.use('dark_background')
	plt.plot(x_arr, y_arr, '^', color='white', alpha = 0.5, markersize = 0.05)
	plt.axis('on')
	plt.show()
	plt.close()

	return


# number of iterations
iterations = int(1e6) 

generate_map(iterations)