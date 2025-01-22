import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    df['login_time'] = pd.to_datetime(df['login_time'])
    df['login_date'] = df['login_time'].dt.date
    return df

def aggregate_features(df):
    login_counts = df.groupby(['user_id', 'login_date']).size().reset_index(name='login_count')
    gameplay_data = df.groupby('user_id').agg({'gameplay_duration': 'mean'}).reset_index()
    return pd.merge(login_counts, gameplay_data, on='user_id')
