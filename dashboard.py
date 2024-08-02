
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from visualization import plot_total_cases, plot_top_countries, plot_daily_cases

@st.cache
def load_data():
    return pd.read_csv('clean_covid_data.csv')

def main():
    st.title('COVID-19 Dashboard')
    df = load_data()

    st.sidebar.header('Filter options')
    date_range = st.sidebar.date_input('Select date range', [])
    countries = st.sidebar.multiselect('Select countries', df['country'].unique())
    case_type = st.sidebar.selectbox('Select case type', ['confirmed', 'deaths', 'recovered'])

    if date_range:
        df = df[(df['date'] >= date_range[0]) & (df['date'] <= date_range[1])]
    if countries:
        df = df[df['country'].isin(countries)]
    
    if case_type:
        df = df[['date', 'country', case_type]]

    st.subheader('Total Cases Over Time')
    plot_total_cases(df)
    st.pyplot(plt.gcf())

    st.subheader('Top 10 Countries')
    plot_top_countries(df)
    st.pyplot(plt.gcf())

    st.subheader('Daily New Cases')
    plot_daily_cases(df)
    st.pyplot(plt.gcf())

if __name__ == "_main_":
    main()