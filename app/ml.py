import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

try:
    # API requests
    tenants_api = requests.get('http://127.0.0.1:8000/tenants/')
    tenants_api.raise_for_status()
    tenants_api_data = tenants_api.json()
    print("Tenants API Response:", tenants_api_data) 

    applications_api = requests.get('http://127.0.0.1:8000/applications/')
    applications_api.raise_for_status()
    applications_api_data = applications_api.json()
    print("Applications API Response:", applications_api_data)

    # Create DataFrames
    tdf = pd.DataFrame(tenants_api_data)
    adf = pd.DataFrame(applications_api_data)

    # Merge DataFrames
    inner_merged_df = pd.merge(tdf, adf, left_on="id", right_on="tenant_id", how="inner")
    print("Merged DataFrame:\n", inner_merged_df.head())

    # 1. Data Preprocessing: Handle missing values
    merged_cleaned = inner_merged_df.dropna()  # Drop rows with missing values
    # Alternatively, fill missing values: merged_cleaned.fillna(value)

    # Drop unnecessary columns (example)
    if 'unnecessary_column' in merged_cleaned.columns:
        merged_cleaned.drop(columns=['unnecessary_column'], inplace=True)

    # 2. Data Cleaning
    # Standardize column names
    merged_cleaned.columns = [col.lower().strip() for col in merged_cleaned.columns]

    # Convert data types if necessary
    if 'age' in merged_cleaned.columns:
        merged_cleaned['age'] = merged_cleaned['age'].astype(int)

    # 3. Feature Engineering
    # Example: Create a new column for application duration
    if 'application_date' in merged_cleaned.columns and 'approval_date' in merged_cleaned.columns:
        merged_cleaned['application_duration'] = pd.to_datetime(
            merged_cleaned['approval_date']
        ) - pd.to_datetime(merged_cleaned['application_date'])
        merged_cleaned['application_duration'] = merged_cleaned['application_duration'].dt.days

    # 4. Standardization and Scaling
    scaler = StandardScaler()
    minmax_scaler = MinMaxScaler()

    # Select numeric columns
    numeric_cols = merged_cleaned.select_dtypes(include=['float64', 'int64']).columns

    # Standardize (mean=0, std=1)
    merged_cleaned[numeric_cols] = scaler.fit_transform(merged_cleaned[numeric_cols])

    # Alternatively, use MinMax scaling (0 to 1 range)
    # merged_cleaned[numeric_cols] = minmax_scaler.fit_transform(merged_cleaned[numeric_cols])

    print("Processed DataFrame:\n", merged_cleaned.head())

except requests.exceptions.RequestException as e:
    print(f"An error occurred while making API requests: {e}")
except KeyError as e:
    print(f"Missing key in the API response: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
