import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

filePath = '../datasets/avocado.csv'

dataset = pd.read_csv(filePath)
#print dataset.describe()
#print dataset.columns

features = ['Total Volume', '4046', '4225', '4770', 'Total Bags']
lenm = len(dataset['4046'].values)
x = [np.ones(lenm)]

for ft in features:
	x.append(dataset[ft].values)

X = np.array(x).T
B = np.array([0 for _ in xrange(len(features)+1)])
Y = dataset['AveragePrice']

def hypo(theta, x):
	h = x.dot(theta)
	return h

def cost_function(theta, x, y):
	m = len(x)
	j = np.sum((x.dot(theta) - y) ** 2) / (2 * m)
	return j

def grad_descent(theta, x, y, alpha):
	m = len(x)
	'''step = 0
	for i in xrange(m):
		desc = 0
		hi = hypo(theta, x[i])
		for j in xrange(len(theta)):
			desc += (hi - y[i])*x[i][j]
	step = alpha * (desc / m)
	return step'''

	h = x.dot(theta)
	loss = h - y
	grad = x.T.dot(loss) / m
	theta = theta - (alpha * grad)
	
	return theta

def trains(x, y, theta, alpha, loops):

	for i in xrange(loops):
		theta = grad_descent(theta, x, y, alpha)
	print theta
	final_cost = cost_function(theta, x, y)
	return final_cost

def trainSK(x, y):
	trainX, testX, trainY, testY = train_test_split(x, y, test_size=0.25, random_state=0)
	model = LinearRegression()
	model.fit(trainX, trainY)
	result = model.predict(testX)
	#print result
	cost = model.score(testX, testY)
	return cost

def main():
	choice = raw_input('''
1. Train the model using the algo built from scratch
2. Train the model using the SKLearn algo.
What is you choice (1/2)? ''')

	loops = input('How many iterations do you need to train model?\t') if choice == "1" else 0

	alpha = 0.01
	print B
	cost = trains(X, Y, B, alpha, loops) if choice == '1' else trainSK(X, Y)
	print 'The cost using the choice {0} is {1}'.format(choice, cost)

if __name__ == '__main__':
	main()	






























