# Import Flask framework
from flask import Flask, request, jsonify

# Create Flask app
app = Flask(__name__)

# Simulated "machine learning model"
def model_predict(data):
    # Use simple sum as a placeholder for prediction
    return sum(data)

# Home route for testing
@app.route("/")
def home():
    return "Application is running successfully!"

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    input_data = request.get_json(force=True)
    values = input_data["data"]
    result = model_predict(values)
    return jsonify({"prediction": result})

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
