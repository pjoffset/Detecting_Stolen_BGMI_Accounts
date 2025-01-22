# Detecting Stolen BGMI Accounts Using Machine Learning

## Project Overview

This project aims to enhance the security of BGMI (Battlegrounds Mobile India) accounts by detecting potential account theft through machine learning techniques. By analyzing user behavior patterns, the system identifies anomalies that may indicate unauthorized access or suspicious activity.

### Key Features:
- **Data Preprocessing**: Load and preprocess user data to extract relevant features.
- **Anomaly Detection**: Utilize the Isolation Forest algorithm to detect unusual behavior patterns in user activity.
- **Real-time Alerts**: Automatically send email notifications to users when suspicious activity is detected.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data Format](#data-format)
- [Contributing](#contributing)

## Technologies Used

- **Python**: The primary programming language used for development.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For implementing machine learning algorithms.
- **Joblib**: For saving and loading trained models.
- **Smtplib**: For sending email alerts.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
`git clone https://github.com/pjoffset/Detecting_Stolen_BGMI_Accounts.git
cd Detecting_Stolen_BGMI_Accounts`

2. **Install dependencies**:
`Create a virtual environment (optional but recommended) and install the required packages:
python -m venv venv
source venv/bin/activate`
 
On Windows use `venv\Scripts\activate
pip install -r requirements.txt`

## Usage

1. **Prepare your data**:
Ensure that your user data is in CSV format with the following columns:
- `user_id`: Unique identifier for each user.
- `login_time`: Timestamp of user login (format: YYYY-MM-DD HH:MM).
- `location`: Geographical location of the user during login.
- `device_id`: Identifier for the device used to log in.
- `gameplay_duration`: Duration of gameplay in minutes.

2. **Run the main script**:
Execute the main script to train the model and detect anomalies:
python main.py

3. **Check for alerts**:
If any anomalies are detected, email alerts will be sent to the specified user email address.

## Data Format

The input data must be structured as follows:

### Example Data (`user_data.csv`)
`user_id,login_time,location,device_id,gameplay_duration
1,2025-01-20 10:00,New York,device_1,30
1,2025-01-20 12:00,New York,device_1,45
1,2025-01-21 10:00,Los Angeles,device_2,60
2,2025-01-20 09:00,New York,device_1,20
2,2025-01-21 14:00,Chicago,device_1,25`


### New Login Data (`new_login_data.csv`)
`user_id,login_count,gameplay_duration
1,3,10`

## Contributing

Contributions are welcome! If you would like to contribute to this project:

1. Fork the repository.
2. Create a new branch (e.g., `feature/your-feature`).
3. Make your changes and commit them.
4. Push your branch and create a pull request.

Please ensure that your code adheres to standard Python coding practices and includes appropriate tests where applicable.
