# 14.Implement a logistic regression model using scikit-learn to classify Heart.csv dataset
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\jayja\Desktop\vsec practice\heart.csv")

# Display the first few rows of the dataset to understand the structure
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Preprocessing: Check if there are any categorical columns and encode them
# In this example, assume 'target' is the column we want to predict, and it's categorical
# Let's assume that all features are numeric, but if they aren't, you might need to encode categorical variables.

# Split the dataset into features (X) and target variable (y)
X = df.drop(columns=['target'])  # Features (all columns except 'target')
y = df['target']  # Target variable (the 'target' column)


# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Logistic Regression model
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train_scaled, y_train)

# Make predictions
y_pred = log_reg.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Plot the confusion matrix as a heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Disease', 'Disease'], yticklabels=['No Disease', 'Disease'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

sns.regplot(x=df['age'], y=df['target'], logistic=True, ci=None, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.show()