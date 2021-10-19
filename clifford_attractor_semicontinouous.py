#! Python3
# A program to observe the behavior of the clifford map 
# as a continuous-like equation system using Euler's 
# approximation

# import third party libraries
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')



def clifford_attractor(x, y, a=-1.4, b=1.7, c=1.0, d=0.7):
	"""
	Returns the change in arguments x and y according to 
	the Clifford map equation. Kwargs a, b, c, and d are specified
	as constants.

	Args:
		x: float, current x coordinate
		y: float, current y coordinate
	kwargs:
		a: float, constant param
		b: float, constant param
		c: float, constant param
		d: float, constant param

	Returns:
		x_next: float, next x coordinate
		y_next: float, next y coordinate

	"""

	x_next = np.sin(a*y) + c*np.cos(a*x) 
	y_next = np.sin(b*x) + d*np.cos(b*y)

	return x_next, y_next


def euler_map(iterations, delta_t):
	"""
	Generate a map of the Clifford Attractor
	
	Args:
		iterations: int, number of steps plotted
		delta_t: float, time step size

	Returns:
		None (shows pyplot figure)
	
	"""

	# initialization
	x_arr, y_arr = [], []

	# starting point at (90, 90)
	x_arr.append(90), y_arr.append(90)


	for i in range(iterations-1):
		dx, dy = clifford_attractor(x_arr[-1], y_arr[-1])
		x_next = x_arr[-1] + dx * delta_t
		y_next = y_arr[-1] + dy * delta_t
		x_arr.append(x_next)
		y_arr.append(y_next)

	# make and display figure.
	plt.style.use('dark_background')
	plt.plot(x_arr, y_arr, '^', color='white', alpha = 0.5, markersize = 0.05)
	plt.axis('on')
	plt.show()
	plt.close()

	return

# parameters, with a deliberately large delta_t step size
steps = 1000000
delta_t = 1.35

euler_map(steps, delta_t)




