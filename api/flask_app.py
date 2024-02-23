from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load models and scalers
encoder = joblib.load('encoders_scalers/encoder.pkl')
scaler = joblib.load('encoders_scalers/scaler.pkl')
model = joblib.load('models/flight_price_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    categorical_features = encoder.transform(df[['from', 'to', 'flightType', 'agency']])
    numerical_features = scaler.transform(df[['time', 'distance']])
    features = np.concatenate([categorical_features.toarray(), numerical_features], axis=1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
