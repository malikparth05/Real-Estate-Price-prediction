from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

# Load model and data columns
model = pickle.load(open('banglore_home_prices_model.pickle', 'rb'))
with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)

@app.route('/')
def home():
    return render_template('index.html', locations=data_columns[3:])

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form['location']
    sqft = float(request.form['sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])

    output = predict_price(location, sqft, bath, bhk)

    return render_template('index.html', prediction_text=f"Estimated Price: ₹ {output} Lakhs", locations=data_columns[3:])

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5006))
    app.run(host='0.0.0.0', port=port)
