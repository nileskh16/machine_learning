import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

main_file_path = '../input/house-prices-advanced-regression-techniques/train.csv' # this is the path to the Iowa data that you will use
data = pd.read_csv(main_file_path)

# Run this code block with the control-enter keys on your keyboard. Or click the blue botton on the left
interested_params = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = data[interested_params]
y = data.SalePrice

trainX, testX, trainY, testY = train_test_split(X, y, random_state = 0)

iowa_model = DecisionTreeRegressor()
iowa_model.fit(trainX, trainY)

print(X.head())
predicted_prices = iowa_model.predict(testX)
error = mean_absolute_error(testY, predicted_prices)
print('Error of the model is around {0}'.format(error))

iowa_forest_model = RandomForestRegressor()
iowa_forest_model.fit(trainX, trainY)
forest_result = iowa_forest_model.predict(textX)
forest_mae = mean_absolute_error(testY, forest_result)
print('The Forest Mean Absolute error is {0}'.format(forest_mae))


def get_mae(max_leaf_nodes, trainX, trainY, testX, testY):
    iowa_model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    iowa_model.fit(trainX, trainY)
    predicted_values = iowa_model.predict(testX)
    mae = mean_absolute_error(testY, predicted_values)
    return mae

for leaf_size in [5, 10, 25, 50]:
    mae = get_mae(leaf_size, trainX, trainY, testX, testY)
    print('For {0} max leaf nodes, we have got {0} MAE'.format(leaf_size, mae))


