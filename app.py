import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

print("🚀 Kidney Disease Prediction Started")

# Load dataset
train_df = pd.read_csv("dataset/train.csv")
test_df = pd.read_csv("dataset/test.csv")

# Split data
X_train = train_df.iloc[:, :-1]
y_train = train_df['class']

X_test = test_df.iloc[:, :-1]
y_test = test_df['class']

# Train model
model = GaussianNB()
model.fit(X_train, y_train)

print("✅ Model trained successfully")

# Predict
predictions = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, predictions)

print("\n📊 Results:")
print("Accuracy:", acc)

print("\n🔍 Sample Predictions:")
print(predictions[:10])
