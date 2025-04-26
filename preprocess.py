# preprocess.py
import pandas as pd
import numpy as np

def load_and_preprocess(filepath):
    df = pd.read_csv(filepath)
    df = df.dropna(subset=['distance', 'cab_type', 'time_stamp', 'destination', 'source', 'price'])
    df['time_stamp'] = pd.to_datetime(df['time_stamp'], unit='ms')
    df['hour'] = df['time_stamp'].dt.hour
    df['dayofweek'] = df['time_stamp'].dt.dayofweek
    df = pd.get_dummies(df, columns=['cab_type', 'destination', 'source', 'name'], drop_first=True)
    X = df.drop(['price', 'id', 'product_id', 'time_stamp'], axis=1)
    y = df['price']
    return X, y
