#! python3
# grid map: an exploration of sensitive
# dependance on initial conditions using 
# a semicontinuous map.  Produces a series of 
# images that can be assembled into a video.

# import third party libraries
import numpy as np
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

#Differential equation
def grid_map(x, y, a=0.1, b=0.1):
	x_n = a * np.cos(y)
	y_n = b * np.sin(x)
	return x_n, y_n

for t in range(600):
	# step parameters
	steps = np.int((1000000 / 600) * t)
	delta_t = 18

	# solution array initialization
	X = np.zeros(steps + 1)
	Y = np.zeros(steps + 1)
	X2 = np.zeros(steps + 1)
	Y2 = np.zeros(steps + 1)

	# Initial position
	X[0], Y[0] = (1, 0)
	X2[0], Y2[0] = (1.000000001, 0)

	#differential equation iterations
	for i in range(steps):
		x_dot, y_dot = grid_map(X[i], Y[i])
		x2_dot, y2_dot = grid_map(X2[i], Y2[i])
		X[i + 1] = X[i] + x_dot * delta_t
		Y[i + 1] = Y[i] + y_dot * delta_t
		X2[i + 1] = X2[i] + x2_dot * delta_t
		Y2[i + 1] = Y2[i] + y2_dot * delta_t


	# x = np.arange(-30, 10, 0.6)
	# y = np.arange(-20, 20, 0.6)

	# X2, Y2 = np.meshgrid(x, y)

	# dx = 0.1 * np.cos(Y2)
	# dy = 0.1 * np.sin(X2)

	# color_array = (np.abs(dx) + np.abs(dy))

	# plot figure
	plt.plot(X, Y, ',', color='red', alpha=0.3, markersize=0.001)
	plt.plot(X2, Y2, ',', color='blue', alpha=0.3, markersize=0.01)

	# plt.quiver(X2, Y2, dx, dy, color_array, scale = 5.7, width=0.0018, alpha=0.4)
	plt.xlim(-800, 1850)
	plt.ylim(-1600, 700)
	plt.axis('off')
	plt.savefig('{}.png'.format(t), dpi=300)
	plt.close()

