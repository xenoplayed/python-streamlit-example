import pickle
import os

DATA_FILE = 'data.pkl'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'rb') as f:
            return pickle.load(f)
    return []


def save_data(data):
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(data, f)
