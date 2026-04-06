from flask import Flask, render_template, request
import pandas as pd
from sklearn.naive_bayes import GaussianNB

# Create app FIRST
app = Flask(__name__)

# Train model
train_df = pd.read_csv("dataset/train.csv")

X_train = train_df.iloc[:, :-1]
y_train = train_df['class']

model = GaussianNB()
model.fit(X_train, y_train)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            'age','bp','sg','al','su',
            'rbc','pc','pcc','ba','bgr',
            'bu','sc','sod','pot','hemo',
            'pcv','wc','rc',
            'htn','dm','cad','appet','pe','ane'
        ]

        values = [float(request.form.get(f)) for f in features]

        input_data = pd.DataFrame([values], columns=features)

        prediction = model.predict(input_data)[0]

        return render_template("index.html", result=prediction)

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
