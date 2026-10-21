import os
import sys

# Add the 'HOUSE PREDICTION MODEL' folder to sys.path
base_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(base_dir, "HOUSE PREDICTION MODEL")
sys.path.insert(0, model_dir)

from app import app

if __name__ == "__main__":
    print("Starting House Price Prediction Web App at http://127.0.0.1:5000 ...")
    app.run(debug=True)
