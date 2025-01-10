import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load your dataset
df = pd.read_csv('data/car_sales.csv')

# Features (X) will be all columns except 'selling_price'
X = df.drop('selling_price', axis=1)  # Now using the correct column name
y = df['selling_price']

# You might need to handle categorical columns like 'name', 'fuel', 'seller_type', 'transmission', 'owner'
# Let's use pandas get_dummies for categorical columns
X = pd.get_dummies(X, columns=['name', 'fuel', 'seller_type', 'transmission', 'owner'])

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
joblib.dump(model, 'car_sales_model.pkl')

print("Model has been trained and saved successfully!")