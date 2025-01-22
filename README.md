# Detecting Stolen BGMI Accounts Using Machine Learning

This project detects stolen BGMI accounts by analyzing user behavior patterns and identifying anomalies using machine learning.

## Features:
- Data preprocessing and feature engineering.
- Anomaly detection using Isolation Forest.
- Real-time alert system for suspicious activities.

## How to Run:
1. Install dependencies:
`pip install -r requirements.txt`

2. Run the main script:
`python main.py`


## Data Format:
User data should be in CSV format with columns:
 `user_id, login_time (YYYY-MM-DD HH:MM), location, device_id, gameplay_duration (minutes)`
