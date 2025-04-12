import pickle 
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

#Load housing data 
data = fetch_california_housing()

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=40)


#Train model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

#Serialize model
with open("data/model.pkl","wb") as f:
    pickle.dump(model, f)

