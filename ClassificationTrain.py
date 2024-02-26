from sklearn.ensemble import RandomForestClassifier

def train_classification_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model
