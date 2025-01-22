from src.data_preprocessing import load_data, preprocess_data, aggregate_features
from src.model_training import train_model, save_model, load_model
from src.anomaly_detection import detect_anomalies
from src.alert_system import send_alert

# Step 1: Load and preprocess data
data = load_data("data/user_data.csv")
data = preprocess_data(data)
features = aggregate_features(data)

# Step 2: Train and save the model (run once)
model = train_model(features)
save_model(model, "model/isolation_forest.pkl")

# Step 3: Load the model and detect anomalies in new data
model = load_model("model/isolation_forest.pkl")
new_data = load_data("data/new_login_data.csv")
anomalies = detect_anomalies(model, new_data)

# Step 4: Send alerts for anomalies
if not anomalies.empty:
    print("Anomalies detected:", anomalies)
    send_alert("user@example.com")
