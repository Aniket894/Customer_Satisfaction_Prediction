from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import pandas as pd
from src.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

class PredictionPipeline:
    def __init__(self, model_path, preprocessor_path):
        # Load the pre-trained model and preprocessor
        self.model = joblib.load(model_path)
        self.preprocessor = joblib.load(preprocessor_path)

    def predict(self, input_data):
        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])
        # Transform the data using the preprocessor
        processed_data = self.preprocessor.transform(input_df)
        # Make predictions using the model
        predictions = self.model.predict(processed_data)
        return predictions.tolist()
    
# Initialize the prediction pipeline with model and preprocessor paths
prediction_pipeline = PredictionPipeline(
    model_path='artifacts/GradientBoostingClassifier.pkl',
    preprocessor_path='artifacts/preprocessor.pkl'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def get_prediction():
    
    input_data = {
        'Gender': request.form.get('Gender'),
        'Customer Type': request.form.get('Customer Type'),
        'Age': int(request.form.get('Age')),
        'Type of Travel': request.form.get('Type of Travel'),
        'Class': request.form.get('Class'),
        'Flight Distance': int(request.form.get('Flight Distance')),
        'Inflight wifi service': int(request.form.get('Inflight wifi service')),
        'Departure/Arrival time convenient': int(request.form.get('Departure/Arrival time convenient')),
        'Ease of Online booking': int(request.form.get('Ease of Online booking')),
        'Gate location': int(request.form.get('Gate location')),
        'Food and drink': int(request.form.get('Food and drink')),
        'Online boarding': int(request.form.get('Online boarding')),
        'Seat comfort': int(request.form.get('Seat comfort')),
        'Inflight entertainment': int(request.form.get('Inflight entertainment')),
        'On-board service': int(request.form.get('On-board service')),
        'Leg room service': int(request.form.get('Leg room service')),
        'Baggage handling': int(request.form.get('Baggage handling')),
        'Checkin service': int(request.form.get('Checkin service')),
        'Inflight service': int(request.form.get('Inflight service')),
        'Cleanliness': int(request.form.get('Cleanliness')),
        'Departure Delay in Minutes': int(request.form.get('Departure Delay in Minutes')),
        'Arrival Delay in Minutes': float(request.form.get('Arrival Delay in Minutes', 0))  # Provide default value if not present
    }

    # Make prediction
    predictions = prediction_pipeline.predict(input_data)
    
    return render_template('results.html', predictions=predictions)
    
if __name__ == '__main__':
    app.run(debug=True)
