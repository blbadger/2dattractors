#! Python3
# Makes a series of images of a clifford attractor at slightly
# difference values of constants a, b, c, or, d.  These images
# may be compiled into a movie to observe how smooth changes
# in parameters lead to abrupt changes in attractor shape and 
# dimension

# import third party libraries
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')
a = 2.1
b = 0.95 
c = -0.5
d = -1

def clifford_attractor(x, y, a, b, c, d):
	'''Returns the change in arguments x and y according to 
	the Clifford map equation. Kwargs a, b, c, and d are specified
	as constants.
	'''
	dx = np.sin(a*y) + c*np.cos(a*x) 
	dy = np.sin(b*x) + d*np.cos(b*y)
	return dx, dy

# parameters, with a deliberately large delta_t step size
steps = 500000

# initialization
X = np.zeros(steps)
Y = np.zeros(steps)

X[0], Y[0] = 1,1


# make and display figure.
for j in range(300):

	# parameters, with a deliberately large delta_t step size
	steps = 500000

	# initialization
	X = np.zeros(steps)
	Y = np.zeros(steps)

	X[0], Y[0] = 1,1

	for i in range(steps-1):
		xd, yd = clifford_attractor(X[i], Y[i], a, b + 0.00033*j, c, d)
		X[i+1] = xd
		Y[i+1] = yd

	plt.plot(X, Y, ',', color='white', alpha = 0.1, markersize = 0.01)
	plt.axis('off')
	plt.savefig('{}.png'.format(j), dpi=300)
	plt.close()
