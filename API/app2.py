# Import the dependencies.
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import os
import pickle
from flask_cors import CORS, cross_origin


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Load the trained model
with open('../Neural_Network_Model/rainfall_model.pkl', 'rb') as file:
    model = pickle.load(file)
CORS(app)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"For the route below, you will be putting in the minimum temperature, maximum temperature, humidity, wind speed, and air pressure.<br/>"
        f"/api/v1.0/<tmin>/<tmax>/<humidity>/<wind>/<pressure><br/>"
        )

@app.route("/api/v1.0/<tmin>/<tmax>/<humidity>/<wind>/<pressure>")
def predict(tmin, tmax, humidity, wind, pressure):

    #Put user-inputs retrieved from Javascript into model
    result = model.predict(np.array([[float(tmin), float(tmax), float(wind), 
                                    float(pressure), float(humidity)]]))
    
    #Use model's prediction to display if it will rain
    if int(result[0])==1:
        prediction = "It is going to rain today"
    else:
        prediction = "It is not going to rain today"
    return jsonify(prediction)
    
if __name__ == '__main__':
    app.run(debug = True)