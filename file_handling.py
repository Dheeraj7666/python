import pandas as pd

def save_clean_data(df, file_path='clean_covid_data.csv'):
    df.to_csv(file_path, index=False)

def load_clean_data(file_path='clean_covid_data.csv'):
    return pd.read_csv(file_path)

df = load_clean_data()
print(df.head())
