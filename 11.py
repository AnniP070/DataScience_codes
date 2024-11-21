# 11. For the dataset Orange_Telecom_Churn_Data, Use Seaborn to create a histogram, box plot, and heatmap.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"C:\Users\jayja\Desktop\vsec practice\Orange_Telecom_Churn_Data.csv")

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Set the style for seaborn
sns.set(style="whitegrid")

# 1. Create a Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data['total_day_minutes'], bins=30, kde=True)
plt.title('Distribution of Total Day Minutes')
plt.xlabel('Total Day Minutes')
plt.ylabel('Frequency')
plt.show()

# 2. Create a Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='churned', y='total_day_minutes', data=data)
plt.title('Box Plot of Total Day Minutes by Churn Status')
plt.xlabel('Churned (True/False)')
plt.ylabel('Total Day Minutes')
plt.show()

# 3. Create a Heatmap
# Compute the correlation matrix
numeric_df = df.select_dtypes(include=['float64', 'int64'])
# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()