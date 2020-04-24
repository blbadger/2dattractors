'''
!# Python3
A program to display the Henon map.
'''

# import third-party libraries
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

def henon_attractor(x, y, a=1.4, b=0.3):
	'''Computes the next step in the Henon 
	map for arguments x, y with kwargs a and
	b as constants.
	'''
	dx = 1 - a * x ** 2 + y
	dy = b * x
	return dx, dy

# number of iterations
steps = 1000000

X = np.zeros(steps + 1)
Y = np.zeros(steps + 1)

# starting point
X[0], Y[0] = 0.3, 0.3

for i in range(steps):
	x_dot, y_dot = henon_attractor(X[i], Y[i])
	X[i+1] = x_dot
	Y[i+1] = y_dot

# display plot
plt.figure(figsize=(30, 30))
plt.plot(X, Y, '^', color='white', alpha = 0.4, markersize=0.1)
plt.axis('off')

plt.show()
plt.close()