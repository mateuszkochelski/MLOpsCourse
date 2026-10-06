import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def load_data():
    return load_iris(return_X_y=True)


def train_model(X_train, Y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)
    return model


def save_model(model, filename):
    joblib.dump(model, filename)


if __name__ == "__main__":
    data = load_data()
    model = train_model(*data)
    save_model(model, "iris_model.joblib")
