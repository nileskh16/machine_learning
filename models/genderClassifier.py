from sklearn import tree

#Training Data [height, weight, shoe_size]
X = [[181, 40, 44], [177, 70, 30], [160, 60, 38], [154, 67, 50], [142, 56, 20], [186, 77, 60], [179, 62, 40]]

#Labels to the given data
Y = ['male', 'male', 'female', 'female', 'male', 'female', 'male']

#classifier

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[127, 76, 87]])
print prediction
