#Multiple Linear Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)

from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv('../datasets/students.csv')

print data.shape

math = data['Math'].values
read = data['Reading'].values
write = data['Writing'].values

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(math, read, write, color='#ef1234')
plt.show()


m = len(math)
x0 = np.ones(m)
X = np.array([x0, math, read]).T
B = np.array([0, 0, 0])
Y = np.array(write)
alpha = 0.0001

def cost_function(X, Y, B):
	m = len(Y)
	J = np.sum((X.dot(B) - Y) ** 2) / (2 * m)
	return J

initial_cost = cost_function(X, Y, B)
print 'Initial Cost is {0}'.format(initial_cost)


def gradient_descent(X, Y, B, alpha, iterations):

	cost_history = [0] * iterations
	m = len(Y)	

	for i in xrange(iterations):
		h = X.dot(B)
		loss = h - Y
		descent = X.T.dot(loss) / m
		B = B - alpha * descent
		cost = cost_function(X, Y, B)
		cost_history[i] = cost
	return B, cost_history

newB, cost_history = gradient_descent(X, Y, B, alpha, 100000)

print 'New theta parameters are '
print newB

print cost_history[-1],



















