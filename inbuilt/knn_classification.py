import pandas as pd
from joblib import load, dump
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay


# train the model
def train_model():
    df = pd.read_csv("../dataset/train.csv")
    X = df.iloc[:, :-1].values
    y = df['class'].values

    clf = KNeighborsClassifier(n_neighbors=5)
    clf.fit(X, y)

    dump(clf, '../model/knn_model_inbuilt.joblib')
    print("Model saved.................")


# predict using saved model
def predict_load_model(X_test, plot=True):
    clf = load('../model/knn_model_inbuilt.joblib')
    predictions = clf.predict(X_test)

    if plot:
        ConfusionMatrixDisplay.from_estimator(clf, X_test, predictions)
        plt.show()

    return predictions


def controller_predict(controller, test_data, test_labels, plot=True):
    clf = load('model/knn_model_inbuilt.joblib')
    predictions = clf.predict(test_data)

    if plot:
        ConfusionMatrixDisplay.from_estimator(clf, test_data, test_labels)
        plt.show()

    return predictions
