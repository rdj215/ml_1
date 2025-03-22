import pickle 
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

#Load housing data 
data = fetch_california_housing()

