from sklearn.ensemble import IsolationForest

def train_model(data):
    model = IsolationForest(contamination=0.1)
    model.fit(data[['login_count', 'gameplay_duration']])
    return model

def save_model(model, file_path):
    import joblib
    joblib.dump(model, file_path)

def load_model(file_path):
    import joblib
    return joblib.load(file_path)
