from inbuilt.naivebayes_classification import train_model, predict_load_model
import pandas as pd

print("🚀 Running Kidney Disease Prediction...")

# Train model
train_model()

# Load test data
df = pd.read_csv("dataset/test.csv")

X_test = df.iloc[:, :-1].values

# Predict
predictions = predict_load_model(X_test, plot=False)

print("✅ Predictions:")
print(predictions[:10])
