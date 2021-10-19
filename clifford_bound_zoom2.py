#! Python3
# A program that displays an evolution of the clifford attractor
# using Euler's formula with deliberately large values of delta_t
# combined with a quiver plot, iterating over larger and larger
# values of delta_t.  Produces a series of .png images that can be 
# assembled into a movie.

# import third party libraries
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

def clifford_attractor(x, y, a=-1.4, b=1.7, c=1.0, d=0.7):
	'''Returns the change in arguments x and y according to 
	the Clifford map equation. Kwargs a, b, c, and d are specified
	as constants.
	'''
	x_next = np.sin(a*y) + c*np.cos(a*x) 
	y_next = np.sin(b*x) + d*np.cos(b*y)
	return x_next, y_next

import copy

def clifford_boundary(max_iterations, t, a=-1.4, b=1.7, c=1.0, d=0.7):
	x_range = 3000
	y_range = 3000

	x_list = np.arange(-2/(2**(t/15)) + 9.829945, 2/(2**(t/15)) + 9.829945, (4/2**(t/15))/x_range)
	y_list = np.arange(2/(2**(t/15)) + 7.8592, -2/(2**(t/15)) + 7.8592, -(4/2**(t/15))/y_range)
	array = np.meshgrid(x_list[:3000], y_list[:3000])

	x2 = np.zeros(x_range)
	y2 = np.zeros(y_range)
	iterations_until_in_basin = np.meshgrid(x2, y2)
	for i in iterations_until_in_basin:
		for j in i:
			j += max_iterations

	not_already_in_basin = iterations_until_in_basin[0] < 10000

	for k in range(max_iterations):
		array_copied = copy.deepcopy(array[0]) # copy array to prevent premature modification of x array

		# henon map applied to array 
		array[0] = array[0] + (1.35)*(np.sin(a*array[1]) + c*np.cos(a*array[0]))
		array[1] = array[1] + (1.35)*(np.sin(b*array_copied) + d*np.cos(b*array[1]))

		# note which array elements are diverging, 
		in_basin = np.abs(array[0] - 10.95) + np.abs(array[1] - 8.1) < 1
		entering_basin = in_basin & not_already_in_basin
		iterations_until_in_basin[0][entering_basin] = k
		not_already_in_basin = np.invert(entering_basin) & not_already_in_basin

	return iterations_until_in_basin[0]

	
# differential trajectory
for t in range(, 500):

	# number of iterations
	iterations = 100000
	delta_t = 1.35

	# initialization
	X = np.zeros(iterations)
	Y = np.zeros(iterations)

	# starting point
	(X[0], Y[0]) = (11.3, 8.5)

	# euler's method for tracking differential equations
	for i in range(iterations-1):
		x_next, y_next = clifford_attractor(X[i], Y[i])
		X[i+1] = X[i] + x_next * delta_t
		Y[i+1] = Y[i] + y_next * delta_t

	plt.plot(X, Y, ',', color='white', alpha = 0.2, markersize = 0.1)
	plt.imshow(clifford_boundary(30 + t//10, t), extent=[-2/(2**(t/15)) + 9.829945, 2/(2**(t/15)) + 9.829945, -2/(2**(t/15)) + 7.8592, 2/(2**(t/15)) + 7.8592], cmap='twilight_shifted', alpha=1)
	plt.axis('off')
	# plt.show()
	plt.savefig('{}.png'.format(t), dpi=400, bbox_inches='tight')
	plt.close()
