import numpy as np

class NeuralNet:

	def __init__(self, x, y):
		self.input = x
		self.w1 = np.random.rand(x.shape[0], 4)
		self.y = y
		self.w2 = np.random.rand(4, 1)
		self.output = np.zeroes(y.shape)

	def feedforward(self, b1, b2):
		self.layer1 = sigmoid(np.dot(self.input, self.w1) + b1)
		self.output = sigmoid(np.dot(self.layer1, self.w2) + b2)
