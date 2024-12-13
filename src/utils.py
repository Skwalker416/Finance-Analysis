import pandas as pd

def load_data(file_path):
    """Load raw data into a Pandas DataFrame."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean and preprocess raw data."""
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    return df
