def detect_anomalies(model, new_data):
    prediction = model.predict(new_data[['login_count', 'gameplay_duration']])
    new_data['anomaly'] = prediction
    return new_data[new_data['anomaly'] == -1]
