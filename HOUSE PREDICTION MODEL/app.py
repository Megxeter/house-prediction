import os
from flask import Flask, render_template, request
import pandas as pd
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "house_price_model.pkl")

app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, "templates"), 
            static_folder=os.path.join(BASE_DIR, "static"))
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET","POST"])
def index():
    prediction=None
    if request.method=="POST":
        data = {
            "longitude":[float(request.form["longitude"])],
            "latitude":[float(request.form["latitude"])],
            "housing_median_age":[float(request.form["housing_median_age"])],
            "total_rooms":[float(request.form["total_rooms"])],
            "total_bedrooms":[float(request.form["total_bedrooms"])],
            "population":[float(request.form["population"])],
            "households":[float(request.form["households"])],
            "median_income":[float(request.form["median_income"])],
            "ocean_proximity":[request.form["ocean_proximity"]],
        }
        prediction = model.predict(pd.DataFrame(data))[0]
    return render_template("index.html", prediction=prediction)

if __name__=="__main__":
    app.run(debug=True)
