import pandas as pd
import matplotlib.pyplot as plt

def load_clean_data(file_path='clean_covid_data.csv'):
    return pd.read_csv(file_path)

def basic_analysis(df):
    total_confirmed = df['Confirmed'].sum()
    total_deaths = df['Deaths'].sum()
    total_recovered = df['Recovered'].sum()
    
    print(f"Total confirmed cases: {total_confirmed}")
    print(f"Total deaths: {total_deaths}")
    print(f"Total recovered cases: {total_recovered}")
    
    top_countries = df.groupby('Country/Region')['Confirmed'].sum().nlargest(5)
    print("Top 5 countries with highest confirmed cases:")
    print(top_countries)
    
    bottom_countries = df.groupby('Country/Region')['Confirmed'].sum().nsmallest(5)
    print("Bottom 5 countries with lowest confirmed cases:")
    print(bottom_countries)

df = load_clean_data()
basic_analysis(df)

df['Date'] = pd.to_datetime(df['Date'])
df_grouped = df.groupby('Date')['Confirmed'].sum().reset_index()
plt.figure(figsize=(10,5))
plt.plot(df_grouped['Date'], df_grouped['Confirmed'])
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title('COVID-19 Confirmed Cases Over Time')
plt.show()
