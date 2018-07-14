from numpy import *

def calculate_error(b, m, points):
	error = 0
	for i in xrange(len(points)):
		x = points[i, 0]
		y = points[i, 1]
		error += (y - (m * x + b)) ** 2
	return error

def step_gradient(current_b, current_m, points, alpha):
	b_grad = 0
	m_grad = 0
	N = float(len(points))

	for i in xrange(len(points)):
		x = points[i, 0]
		y = points[i, 1]
		b_grad += -(2/N) * (y - (current_m * x + current_b))
		m_grad += -(2/N) * x * (y - (current_m * x + current_b))
	new_b = current_b - (alpha * b_grad)
	new_m = current_m - (alpha * m_grad)

	return [new_b, new_m]

def gradient_descent_runner(points, start_b, start_m, alpha, iterations):
	b = start_b
	m = start_m

	for i in xrange(iterations):
		b, m = step_gradient(b, m, array(points), alpha)
	return [b, m]

def main():
	print 'Running gradient descent over given data set'
	points = genfromtxt("../datasets/cycling_vs_calories.csv", delimiter=',')
	init_b = 0
	init_m = 0
	num_iter = 2504
	alpha = 0.0001
	print 'Before running Gradient descent, b = {0}, m = {1} and error = {2}'.format(init_b, init_m, calculate_error(init_b, init_m, points))
	b, m = gradient_descent_runner(points, init_b, init_m, alpha, num_iter)
	print 'After {0} iterations, b = {1}, m = {2}, and error = {3}'.format(num_iter, b, m, calculate_error(b, m, points))

if __name__ == '__main__':
	main()





		
		
