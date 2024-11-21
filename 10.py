#10. Use the dataset Iris.csv, Perform basic exploratory data analysis (EDA) and visualize the findings using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
df = pd.read_csv(r"C:\Users\jayja\Desktop\vsec practice\iris.csv")

# Display basic info
print(df.info())
print(df.head())

# 1. Histogram of each numeric feature
df.hist(figsize=(10, 8), bins=15, edgecolor='black')
plt.suptitle("Feature Distributions")
plt.show()

# 2. Scatter plot between Sepal Length and Sepal Width
plt.figure(figsize=(6, 4))
sns.scatterplot(x="SepalLengthCm", y="SepalWidthCm", data=df, hue="Species")
plt.title("Sepal Length vs Sepal Width")
plt.show()

# 3. Line plot of Petal Length across the dataset (just to show a simple line)
plt.figure(figsize=(6, 4))
sns.lineplot(x=df.index, y="PetalLengthCm", data=df, hue="Species")
plt.title("Petal Length across Samples")
plt.show()

# 5. Boxplot of Petal Length by Species
plt.figure(figsize=(10, 6))
sns.boxplot(x="Species", y="PetalLengthCm", data=df)
plt.title("Petal Length by Species")
plt.show()

# 4. Correlation Heatmap
numeric_df = df.select_dtypes(include=[float, int])  # Select only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt='.2f')
plt.title("Feature Correlation Heatmap")
plt.show()

