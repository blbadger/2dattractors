#! python3
# grid map: an exploration of sensitive
# dependance on initial conditions using 
# a semicontinuous map.

# import third party libraries
import numpy as np
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

#Differential equation
def grid_map(x, y, a=0.1, b=0.1):
	x_n = a * np.cos(y)
	y_n = b * np.sin(x)
	return x_n, y_n

# step parameters
steps = 1000000
delta_t = 1

# solution array initialization
X = np.zeros(steps + 1)
Y = np.zeros(steps + 1)

# Initial position
X[0], Y[0] = (1.000000000, 0)

#differential equation iterations
for i in range(steps):
	x_dot, y_dot = grid_map(X[i], Y[i])
	X[i + 1] = X[i] + x_dot * delta_t
	Y[i + 1] = Y[i] + y_dot * delta_t

# plot figure
plt.figure(figsize=(10,10))
plt.plot(X, Y, '^', color='white', alpha=2, markersize=0.1)
plt.axis('on')
plt.show()
plt.close()

