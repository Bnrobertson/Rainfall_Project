# Import the dependencies.
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
# from tensorflow.keras.applications.vgg16 import preprocess_input
import os
from flask_cors import CORS, cross_origin


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
model = load_model('../Neural_Network_Model/rainfall_model.h5', compile = False)
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

    #if request.method == ["POST"]:
    
    result = model.predict(np.array([[float(tmin), float(tmax), float(wind), float(pressure), float(humidity)]]))
    if int(result[0])==1:
        prediction = "It is going to rain today"
    else:
        prediction = "It is not going to rain today"
    return prediction
    #return jsonify(result.tolist())

if __name__ == '__main__':
    app.run(debug = True)