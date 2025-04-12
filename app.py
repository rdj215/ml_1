from fastapi import FastAPI
from pydantic import BaseModel
import pickle 
import numpy as np

#Deserialize model
with open("data/model.pkl","rb") as f:
	model = pickle.load(f)

#Create FastAPI instance
app = FastAPI()

#Create input data model
class InputData(BaseModel):
	data: list[list[float]]


@app.get("/")
def home():
	return {"message": "ML Model API currently running"}

@app.post("/predict/")
def predict(input_data: InputData):
	prediction = model.predict(np.array(input_data.data)).tolist()
	return {"prediction": prediction}


