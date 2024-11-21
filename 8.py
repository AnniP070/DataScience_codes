#8.For the dataset Heart.csv, Use Python to handle missing values by dropping rows, filling with a specific value, 
# and filling with the mean of the column. Display the data frame after each operation.
import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\jayja\Desktop\vsec practice\heart.csv")

# Display the first few rows of the dataset
print("Original Dataset:\n", df.head())

# Check for missing values
print("\nMissing values in each column before handling:\n", df.isnull().sum())

# 1. Drop rows with missing values
df_dropna = df.dropna()

# Display the DataFrame after dropping rows with missing values
print("\nData after dropping rows with missing values:\n", df_dropna.head())

# Check missing values again
print("\nMissing values after dropping rows:\n", df_dropna.isnull().sum())

# 2. Fill missing values with a specific value (e.g., 0)
df_fill_zero = df.fillna(0)

# Display the DataFrame after filling missing values with 0
print("\nData after filling missing values with 0:\n", df_fill_zero.head())

# Check missing values again
print("\nMissing values after filling with 0:\n", df_fill_zero.isnull().sum())

# 3. Fill missing values with the mean of the column
df_fill_mean = df.copy()  # Create a copy to avoid modifying the original data
for column in df.columns:
    if df[column].dtype in ['float64', 'int64']:  # Only fill numeric columns
        mean_value = df[column].mean()
        df_fill_mean[column] = df[column].fillna(mean_value)

# Display the DataFrame after filling missing values with the mean
print("\nData after filling missing values with the mean of the column:\n", df_fill_mean.head())

# Check missing values again
print("\nMissing values after filling with the mean:\n", df_fill_mean.isnull().sum())
