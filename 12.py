#12. For the iris.csv dataset, calculate the correlation matrix and visualize it using a heatmap. Clean the given dataset.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
df = pd.read_csv("iris.csv")

# Display basic info about the dataset
print(df.info())
print(df.head())

# Clean the dataset (handle missing values, if any)
# Check for missing values
print(df.isnull().sum())

# If there are missing values, we can drop rows or fill them (here we drop rows with NaN values)
df = df.dropna()  # Drop rows with missing values

# 1. Calculate the correlation matrix for numeric columns
# numeric_df = df.select_dtypes(include=[float, int])  # Select only numeric column
numeric_df=df.iloc[:, :-1] #row,column
# 2. Visualize the correlation matrix using a heatmap
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt='.2f')
plt.title("Correlation Matrix Heatmap for Iris Dataset")
plt.show()
