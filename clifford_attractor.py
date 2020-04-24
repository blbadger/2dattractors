#! Python3
# A program to observe the behavior of the clifford map 
# as a continuous-like equation system using Euler's 
# approximation. 

# import third party libraries
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

def clifford_attractor(x, y, a=-1.4, b=1.7, c=1.0, d=0.7):
	'''Returns the change in arguments x and y according to 
	the Clifford map equation. Kwargs a, b, c, and d are specified
	as constants.
	'''
	dx = np.sin(a*y) + c*np.cos(a*x) 
	dy = np.sin(b*x) + d*np.cos(b*y)
	return dx, dy

# parameters, with a deliberately large delta_t step size
steps = 1000000
delta_t = 1.35

# initialization
X = np.zeros(steps + 1)
Y = np.zeros(steps + 1)

X[0], Y[0] = 90, 90

# euler's method for tracking differential equations
for i in range(steps):
	xd, yd = clifford_attractor(X[i], Y[i])
	X[i+1] = X[i] + xd * delta_t
	Y[i+1] = Y[i] + yd * delta_t

# make and display figure.
plt.figure(figsize=(10, 10))
plt.plot(X, Y, '^', color='white', alpha = 0.5, markersize = 0.05)
plt.axis('on')
plt.show()
plt.close()



