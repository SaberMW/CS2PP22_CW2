# CS2PP22_CW2
4. Data Pre-Processing

   # Data manipulation 1 (potential integration of module code)
import pandas as pd

def preprocess_data(url):
    # Load the dataset
    column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 
                    'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
    data = pd.read_csv(url, names=column_names, na_values=' ?')  # Missing values are marked as ' ?'

    # Handling Missing Values
    # Check for missing values
    missing_values = data.isnull().sum()
    print("Missing Values:\n", missing_values)

    # Drop rows with missing values
    data_cleaned = data.dropna()

    # Encoding Categorical Variables
    # Encode categorical variables using one-hot encoding
    data_encoded = pd.get_dummies(data_cleaned, columns=['workclass', 'education', 'marital-status', 'occupation', 
                                                        'relationship', 'race', 'sex', 'native-country'])
    
    return data_encoded


# Data# Import the pre-processing function
from data_preprocessing import preprocess_data

# URL of the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

# Call the pre-processing function
preprocessed_data = preprocess_data(url)

# Display the pre-processed data
preprocessed_data.head()
