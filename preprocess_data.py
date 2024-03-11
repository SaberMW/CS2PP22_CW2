# save this code into a file named preprocess_data.py

import pandas as pd

def preprocess_suicide_data(file_path):
    # Load the data
    data = pd.read_csv(file_path)

    # Dropping unnecessary columns
    data = data.drop(['country-year', 'HDI for year', 'generation'], axis=1)

    # Renaming columns for better readability
    data = data.rename(columns={' gdp_for_year ($) ': 'gdp_for_year', 'gdp_per_capita ($)': 'gdp_per_capita'})

    # Converting 'gdp_for_year' column to numerical format
    data['gdp_for_year'] = data['gdp_for_year'].str.replace(',', '').astype(float)

    # Converting 'year' column to datetime format
    data['year'] = pd.to_datetime(data['year'], format='%Y')

    return data
