
import argparse
import subprocess
from data_cleaning import clean_data
from visualization import plot_total_cases, plot_top_countries, plot_daily_cases

def main():
    parser = argparse.ArgumentParser(description='COVID-19 Data Analysis')
    parser.add_argument('--clean', action='store_true', help='Clean the raw data')
    parser.add_argument('--visualize', action='store_true', help='Create visualizations')
    parser.add_argument('--dashboard', action='store_true', help='Run the Streamlit dashboard')

    args = parser.parse_args()

    if args.clean:
        clean_data('raw_covid_data.csv', 'clean_covid_data.csv')
    if args.visualize:
        df = pd.read_csv('clean_covid_data.csv')
        plot_total_cases(df)
        plot_top_countries(df)
        plot_daily_cases(df)
    if args.dashboard:
        subprocess.run(["streamlit", "run", "dashboard.py"])

main()