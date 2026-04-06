import pandas as pd
from joblib import load, dump
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from sklearn.naive_bayes import GaussianNB


# Training model using sklearn classifier
def train_model():
    """Data set reading"""
    df = pd.read_csv("dataset/train.csv")
    X = df.iloc[:, :-1].values
    y = df['class'].values

    clf = GaussianNB()
    clf.fit(X, y)

    dump(clf, '../model/nb_model_inbuilt.joblib')
    print("Model saved.................")


# Predicting using the saved model
def predict_load_model(X_test, plot=True):
    clf = load('../model/nb_model_inbuilt.joblib')
    predictions = clf.predict(X_test)

    if plot:
        ConfusionMatrixDisplay.from_estimator(clf, X_test, predictions)
        plt.show()

    return predictions


def controller_predict(controller, test_data, test_labels, plot=True):
    clf = load('model/nb_model_inbuilt.joblib')
    predictions = clf.predict(test_data)

    if plot:
        ConfusionMatrixDisplay.from_estimator(clf, test_data, test_labels)
        plt.show()

    return predictions
