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


for t in range(1, 450):
	# number of iterations
	iterations = 500000
	delta_t = 0.1 + (1.25/450) * t

	# initialization
	X = np.zeros(iterations)
	Y = np.zeros(iterations)

	# starting point
	(X[0], Y[0]) = (10.75, 8.2)

	# euler's method for tracking differential equations
	for i in range(iterations-1):
		x_next, y_next = clifford_attractor(X[i], Y[i])
		X[i+1] = X[i] + x_next * delta_t
		Y[i+1] = Y[i] + y_next * delta_t

	# Vector plot initialization
	x = np.arange(10.7, 11.2, 1/80)
	y = np.arange(7.6, 8.4, 1/35)

	XX, YY = np.meshgrid(x, y)

	# calculate each vector's size and direction

	a = -1.4
	b = 1.7
	c = 1.0
	d = 0.7

	dx = np.sin(a*YY) + c*np.cos(a*XX)
	dy = np.sin(b*XX) + d*np.cos(b*YY)

	color_array = (np.abs(dx) + np.abs(dy))**0.7

	# make and display figure
	# plt.figure(figsize=(10, 10))

	# differential trajectory
	plt.plot(X, Y, '^', color='white', alpha = 0.9, markersize = 0.03)
	plt.xlim(10.7, 11.2)
	plt.ylim(7.6, 8.4)
	# vector plot
	plt.quiver(XX, YY, dx, dy, color_array, scale = 18, width=0.0018, alpha = 0.8)
	plt.axis('off')
	plt.savefig('{}.png'.format(t), dpi=300)
	plt.close()


