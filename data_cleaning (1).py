import pandas as pd

class DataCleaningError(Exception):
    pass

def clean_data(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        df.dropna(inplace=True)  
        df.to_csv(output_file, index=False)
    except Exception as e:
        raise DataCleaningError(f"Error occurred while cleaning data: {e}")

if __name__ == "_main_":
    input_file = 'country_wise_latest '
    output_file = 'clean_covid_data.csv'
    clean_data(input_file, output_file)
