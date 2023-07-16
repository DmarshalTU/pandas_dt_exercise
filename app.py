import os
from dotenv import load_dotenv
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load environment variables
load_dotenv()

# Define global variables
FEATURES = ['NUM_CHILDREN', 'SALARY_PER_MONTH', 'CAR_VALUE', 'Years_of_education']

def read_data():
    """Function to read data from Excel and CSV files into pandas DataFrames."""
    df1 = pd.read_excel(os.getenv("EXCEL_FILE_PATH"))
    df2 = pd.read_csv(os.getenv("CSV_FILE_PATH"))
    return df1, df2

def handle_missing_values(df1, df2):
    """Function to handle missing values in the datasets."""
    for feature in FEATURES:
        if feature in df1.columns:
            df1[feature].fillna(df1[feature].mean(), inplace=True)
        if feature in df2.columns:
            df2[feature].fillna(df2[feature].mean(), inplace=True)
    return df1, df2

def merge_data(df1, df2):
    """Function to merge two pandas DataFrames on the 'ID' column."""
    return pd.merge(df1, df2, on='ID')

def standardize_features(df):
    """Function to standardize the features to have mean=0 and variance=1."""
    x = df.loc[:, FEATURES].values
    return StandardScaler().fit_transform(x)

def apply_pca(x):
    """Function to apply PCA and get the first principal component."""
    return PCA(n_components=1).fit_transform(x)

def main():
    # Read data
    df1, df2 = read_data()
    
    # Handle missing values
    df1, df2 = handle_missing_values(df1, df2)
    
    # Merge data
    df = merge_data(df1, df2)
    
    # Standardize features
    x = standardize_features(df)
    
    # Apply PCA and get PCA Score
    df['PCA_Score'] = apply_pca(x)
    
    # Print the DataFrame
    print(df)

if __name__ == "__main__":
    main()