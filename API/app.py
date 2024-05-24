# Import the dependencies.
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
import os
from tensorflow.keras.preprocessing import image

#################################################
# Flask Setup
#################################################
### Change model name to load
### Seriously, do this!
app = Flask(__name__)
model = load_model('rainfall_model.h5')

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
        if int(result)==1:
            prediction = "It is going to rain today"
        else:
            prediction = "It is not going to rain today"
        return prediction