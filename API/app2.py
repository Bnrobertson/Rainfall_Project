# Import the dependencies.
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
# from tensorflow.keras.applications.vgg16 import preprocess_input
import os
import pickle
from flask_cors import CORS, cross_origin


#################################################
# Flask Setup
#################################################
### Change model name to load
### Seriously, do this!
app = Flask(__name__)

# Load the trained model
with open('../Neural_Network_Model/rainfall_model.pkl', 'rb') as file:
    model = pickle.load(file)
#model = load_model('../Neural_Network_Model/rainfall_model.h5', compile = False)
CORS(app)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/<tmin>/<tmax>/<humidity>/<wind>/<pressure><br/>"
        )

@app.route("/api/v1.0/<tmin>/<tmax>/<humidity>/<wind>/<pressure>")
def predict(tmin, tmax, humidity, wind, pressure):

    if request.method == "POST":
        result = model.predict([tmin, tmax, humidity, wind, pressure])
        if int(result[0])==1:
            prediction = "It is going to rain today"
        else:
            prediction = "It is not going to rain today"
        return prediction