import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)

data = pd.read_csv('../datasets/headbrain.csv')

print(data.shape)

X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values


#calculate b0 and b1

mean_x = np.mean(X)
mean_y = np.mean(Y)

m = len(X)

numer = 0; denom = 0

for i in xrange(m):
	numer += (X[i] - mean_x) * (Y[i] - mean_y)
	denom += (X[i] - mean_x) ** 2

b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

print 'b0 and b1 are {0} and {1}'.format(b0, b1)

# therefore linear model is Brain Weight = b0 + b1 * HeadSize

max_x = np.max(X) + 100
min_x = np.min(X) - 100

x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x

plt.plot(x, y, color='#58b970', label='Regression Line')
plt.scatter(X, Y, color='#ef5423', label='Scatter Plot')

plt.xlabel('Head Size in cm^3')
plt.ylabel('Brain Weight')
plt.legend()
plt.show()

#cost function

crms = 0
sst = ssr = 0
for i in xrange(m):
	y_pred = b0 + b1 * X[i]
	crms += (Y[i] - y_pred) ** 2
	ssr += (Y[i] - y_pred) ** 2
	sst += (Y[i] - mean_y) ** 2

rmse = np.sqrt(crms/m)
r2 = 1 - (ssr/sst)

print 'RMSE is {0} and score is {1}'.format(rmse, r2)





















