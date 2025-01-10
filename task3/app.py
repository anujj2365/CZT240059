from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import traceback

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load('car_sales_model.pkl')
except Exception as e:
    print(f"Error loading model: {str(e)}")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Received prediction request")  # Debug log
        features = request.form['features'].split(',')
        print(f"Features received: {features}")  # Debug log

        # Create DataFrame
        input_data = pd.DataFrame([{
            'name': features[0].strip(),
            'year': int(features[1].strip()),
            'km_driven': int(features[2].strip()),
            'fuel': features[3].strip(),
            'seller_type': features[4].strip(),
            'transmission': features[5].strip(),
            'owner': features[6].strip()
        }])

        print("Input DataFrame created")  # Debug log

        # Get the same columns as training data
        input_encoded = pd.get_dummies(input_data)
        print(f"Encoded columns: {input_encoded.columns}")  # Debug log

        prediction = model.predict(input_encoded)
        print(f"Prediction made: {prediction}")  # Debug log

        return jsonify({'prediction': f'Predicted Price: ₹{prediction[0]:,.2f}'})

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print(traceback.format_exc())  # Print full traceback
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)