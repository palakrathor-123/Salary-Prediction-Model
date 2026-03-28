import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score


# Load dataset
df = pd.read_csv("data/salary_dataset.csv")

# Split features and target
X = df.drop("Salary", axis=1)
y = df["Salary"]

# Encode categorical columns
encoders = {}
categorical_cols = ["Education Level", "Job Role", "Location"]

for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = Ridge()
model.fit(X_train, y_train)

# Accuracy score
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)

print("✅ Model trained successfully")
print("✅ Accuracy:", score)

# Create models folder
os.makedirs("models", exist_ok=True)

# Save model
with open("models/best_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save encoders
with open("models/encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

print("✅ best_model.pkl and encoders.pkl saved")