# 9.Use the dataset heart, Use Python to identify outliers using the Z-score method and remove the outliers and display the cleaned DataFrame.
import pandas as pd
import numpy as np
from scipy import stats

# Load the Heart Disease dataset
df = pd.read_csv(r"C:\Users\jayja\Desktop\vsec practice\heart.csv")

# Display the original DataFrame
print("Original DataFrame:")
print(df.head())

# Calculate Z-scores for all numeric columns
z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))  # Apply to numeric columns
threshold = 3  # Outliers are Z-scores > 3
outliers = (z_scores > threshold).any(axis=1)  # Identify rows with any outlier

# Remove outliers
cleaned_df = df[~outliers]

# Display the cleaned DataFrame
print("\nCleaned DataFrame:")
print(cleaned_df.head())

# Show number of rows before and after removing outliers
print("\nOriginal DataFrame shape:", df.shape)
print("Cleaned DataFrame shape:", cleaned_df.shape)
