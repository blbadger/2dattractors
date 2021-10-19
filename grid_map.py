#! python3
# grid map: an exploration of sensitive
# dependance on initial conditions using 
# a semicontinuous map.

# import third party libraries
import numpy as np
import matplotlib.pyplot as plt 
plt.style.use('dark_background')



def grid_map(x, y, a=0.1, b=0.1):
	"""
	Differential equation to produce the grid map

	Args:
		x: float
		y: float
	kwargs:
		a: float, parameter
		b: float, parameter

	Returns:
		x_n: float, next x value
		y_n: float, next y value

	"""

	x_n = a * np.cos(y)
	y_n = b * np.sin(x)

	return x_n, y_n

def produce_grid(steps, delta_t):
	"""
	Display a grid map trajectory using Euler's method

	Args:
		steps: int, number of iterations
		delta_t: float, size of time step

	Returns:
		None

	"""
	# solution array initialization
	x_arr, y_arr = [], []

	# Initial position
	x_arr.append(1.000000) , y_arr.append(0)

	# differential equation iterations
	for i in range(steps):
		current_x, current_y = x_arr[-1], y_arr[-1]

		x_dot, y_dot = grid_map(current_x, current_y)
		x_arr.append(current_x + x_dot * delta_t)
		y_arr.append(current_y + y_dot * delta_t)


	# plot figure
	plt.figure(figsize=(10,10))
	plt.plot(x_arr, y_arr, '^', color='white', alpha=2, markersize=0.1)
	plt.axis('on')
	plt.show()
	plt.close()


# step parameters
steps = 1000000
delta_t = 1

produce_grid(steps, delta_t)