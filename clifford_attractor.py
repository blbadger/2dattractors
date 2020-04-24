#! Python3
# A program to observe the behavior of the clifford map.
# Based on Vedran Sekara's post found here:
# https://vedransekara.github.io/2016/11/14/strange_attractors.html

# import third party libraries
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

def clifford_attractor(x, y, a=-2.1, b=-0.8, c=1.2, d=1.6):
	'''Returns the change in arguments x and y according to 
	the Clifford map equation. Kwargs a, b, c, and d are specified
	as constants.
	'''
	x_next = np.sin(a*y) + c*np.cos(a*x) 
	y_next = np.sin(b*x) + d*np.cos(b*y)
	return x_next, y_next

# number of iterations
iterations = 1000000

# initialization
X = np.zeros(iterations)
Y = np.zeros(iterations)

# starting point
X[0], Y[0] = 1, 1

# euler's method for tracking differential equations
for i in range(iterations-1):
	x_next, y_next = clifford_attractor(X[i], Y[i])
	X[i+1] = x_next
	Y[i+1] = y_next 

# make and display figure.
plt.figure(figsize=(10, 10))
plt.plot(X, Y, '^', color='white', alpha = 0.5, markersize = 0.05)
plt.axis('on')
plt.show()
plt.close()