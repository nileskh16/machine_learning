import numpy as np
import pandas as pd
import math
from numpy import loadtxt, where
import matplotlib.pyplot as pyt
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

def readAndCleanData():
	min_max_scaler = preprocessing.MinMaxScaler(feature_range=(-1,1))
	df = pd.read_csv("../datasets/grader.csv", header=0)
	df.columns = ['grade1', 'grade2', 'label']
	x = df['label'].map(lambda x: float(x.rstrip(';')))
	X = df[['grade1', 'grade2']]
	X = np.array(X)
	X = min_max_scaler.fit_transform(X)
	Y = df['label'].map(lambda x: float(x.rstrip(';')))
	Y = np.array(Y)

	return [X, Y]


def sigmoid(z):
	sig = float(1 / float(1 + math.exp(-1 * z)))
	return sig

def Hypothesis(theta, X):
	z = 0
	for i in xrange(len(X)):
		z += theta[i] * X[i]
	return sigmoid(z)

def cost_function(X, Y, theta):
	m = len(X)
	sumError = 0
	for i in xrange(m):
		hi = Hypothesis(theta, X[i])
		#print 'Hypothesis is {0}'.format(hi)
		if Y[i] == 1:
			error = Y[i] * math.log(hi)
		elif Y[i] == 0:
			error = (1-Y[i]) * math.log(1-hi)
		sumError += error
	constant = float(-1 / m)
	cost = constant * sumError
	return cost

def Gradient(X, Y, theta, m, alpha, j):
	grad = 0
	for i in xrange(m):
		xi = X[i]
		xij = xi[j]
		hi = Hypothesis(theta, xi)
		grad += (hi - Y[i]) * xij
	constant = float(alpha/m)
	descent = grad * constant
	return descent

def gradient_derivative(X, Y, theta, alpha):
	new_theta = []
	
	for j in xrange(len(theta)):
		nTheta = theta[j]
		gradj = Gradient(X, Y, theta, len(X), alpha, j)
		nTheta -= gradj
		new_theta.append(nTheta)

	return new_theta

def TrainModel(X, Y, theta, alpha, iterations):
	new_theta = theta

	for i in xrange(iterations):
		new_theta = gradient_derivative(X, Y, new_theta, alpha)
	final_cost = cost_function(X, Y, new_theta)
	return {'theta': new_theta, 'cost': final_cost}

def main():
	X, Y = readAndCleanData()
	alpha = 0.1
	init_theta = [0, 0]
	iterations = 1000
	output = TrainModel(X, Y, init_theta, alpha, iterations)
	final_theta = output['theta']
	new_hi = Hypothesis(final_theta, [28.55, 27.63])
	print 'Student will surely pass with probability of {0} and cost is {1}'.format(new_hi, output)

if __name__ == '__main__':
	main()


















