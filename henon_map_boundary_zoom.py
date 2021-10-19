

# import third-party libraries
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')
import copy



def henon_map(max_iterations, a, b, x_range, y_range):
	xl = -40/(2**(t/15)) + 0.4564
	xr = 40/(2**(t/15)) + 0.4564
	yl = 40/(2**(t/15)) - 0.50202
	yr = -40/(2**(t/15)) - 0.50202

	x_list = np.arange(xl, xr, (xr - xl)/x_range)
	y_list = np.arange(yl, yr, -(yl - yr)/y_range)
	array = np.meshgrid(x_list, y_list)

	x2 = np.zeros(x_range)
	y2 = np.zeros(y_range)
	iterations_until_divergence = np.meshgrid(x2, y2)

	for i in iterations_until_divergence:
		for j in i:
			j += max_iterations

	# make an array with all elements set to 'True'
	not_already_diverged = array[0] < 1000

	for k in range(max_iterations):
		array_copied = copy.deepcopy(array[0]) # copy array to prevent premature modification of x array

		# henon map applied to array 
		array[0] = 1 - a * array[0]**2 + array[1]
		array[1] = b * array_copied

		# note which array elements are diverging, 
		r = (array[0]**2 + array[1]**2)**0.5
		diverging = r > 10 
		diverging_now = diverging & not_already_diverged
		iterations_until_divergence[0][diverging_now] = k
		not_already_diverged = np.invert(diverging_now) & not_already_diverged

		# prevent explosion to infinity
		array[0][diverging] = 0
		array[1][diverging] = 0

	return iterations_until_divergence[0]

x_range = 2000
y_range = 2000
for t in range(300):
	# There is an off-by-one error when assigning x_list and y_list values
	while True:
		end = True
		try: plt.imshow(henon_map(70 + t, a=0.2, b=-1.1, x_range=x_range, y_range = y_range), extent=[-40/(2**(t/15)) + 0.4564, 40/(2**(t/15))+ 0.4564, -40/(2**(t/15))- 0.50202,40/(2**(t/15))- 0.50202], cmap='twilight_shifted')
		except IndexError:
			x_range += 1
			y_range += 1
			end = False
		if end: break

	plt.axis('off')
	plt.savefig('{}.png'.format(t), dpi=300)
	plt.close()

