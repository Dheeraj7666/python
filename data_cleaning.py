import pandas as pd
from datetime import datetime
import numpy as np

class DataCleaningError(Exception):
    pass

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise DataCleaningError(f"Error loading data: {e}")

def clean_data(df):
    try:
        df.fillna({
            'Recovered': 0,
            'Deaths': 0,
            'Confirmed': 0
        }, inplace=True)
        
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
        df.columns = [col.strip() for col in df.columns]
        
        return df
    except Exception as e:
        raise DataCleaningError(f"Error cleaning data: {e}")

file_path = 'covid_19_data.csv' 
df = load_data(file_path)
cleaned_df = clean_data(df)
cleaned_df.to_csv('clean_covid_data.csv', index=False)
print("Data cleaning completed and saved to clean_covid_data.csv")
