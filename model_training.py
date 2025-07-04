import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Create mock Indian housing dataset
np.random.seed(42)
data = {
    'location': np.random.randint(0, 4, 1000),  # 0: Tier-3, 1: Tier-2, 2: Tier-1, 3: Metro
    'size_sqft': np.random.randint(500, 5000, 1000),
    'bedrooms': np.random.randint(1, 5, 1000),
    'bathrooms': np.random.randint(1, 4, 1000),
    'parking': np.random.randint(0, 3, 1000),
    'furnishing': np.random.randint(0, 3, 1000),  # 0: Unfurnished, 1: Semi, 2: Fully
}

df = pd.DataFrame(data)
# Assume a synthetic price formula (randomized)
df['price_in_lakhs'] = (
    df['size_sqft'] * 0.002 +
    df['bedrooms'] * 5 +
    df['bathrooms'] * 3 +
    df['parking'] * 2 +
    df['furnishing'] * 3 +
    df['location'] * 4 +
    np.random.normal(0, 5, 1000)
)

X = df.drop('price_in_lakhs', axis=1)
y = df['price_in_lakhs']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.2f} lakhs")
print(f"R² Score: {r2:.2f}")

# Save model
joblib.dump(model, 'indian_house_model.pkl')
print("Model saved as 'indian_house_model.pkl'")
