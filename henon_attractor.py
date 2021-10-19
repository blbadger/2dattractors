# henon_attractor.py
# A program to display the Henon map.

# import third-party libraries
import numpy as np 
import matplotlib.pyplot as plt 

def henon_attractor(x, y, a=1.4, b=0.3):
	'''Computes the next step in the Henon map

	Args:
		x: float, current x value
		y: float, current y value
	kwargs:
		a, b: float, constants

	Returns:
		x_next: float, current x value
		y_next: flaot, current y value
	'''

	x_next = 1 - a * x ** 2 + y
	y_next = b * x

	return x_next, y_next


def map_henon(steps):
	"""
	Produce the Henon map

	Args:
		steps: int, number of iterations

	Returns:
		None

	"""

	x_arr, y_arr = [], []

	# starting point
	x_arr.append(0.3), y_arr.append(0.3)

	for i in range(steps):
		x_next, y_next = henon_attractor(x_arr[-1], y_arr[-1])
		x_arr.append(x_next)
		y_arr.append(y_next)

	# display plot
	plt.style.use('dark_background')
	plt.plot(x_arr, y_arr, '^', color='white', alpha = 0.4, markersize=0.1)
	plt.axis('off')

	plt.show()
	plt.close()


# number of iterations
steps = 1000000
map_henon(steps)