# 15. Implement a linear regression model using scikit-learn to predict house prices.
#  a. housing.csv
# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load the dataset
data = pd.read_csv('housing.csv')
print(data.head())

# Step 2: Data Preprocessing
# Dropping rows with missing values
data = data.dropna()
print(data.head())

# Converting the 'ocean_proximity' categorical column to numerical format using one-hot encoding
data = pd.get_dummies(data, columns=['ocean_proximity'], drop_first=True)

# Separate features and target variable
# Setting 'median_house_value' as the target column for prediction
X = data.drop('median_house_value', axis=1)  # Features
y = data['median_house_value']               # Target

# Step 3: Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Initialize and Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make Predictions on the Test Set
y_pred = model.predict(X_test)

# Step 6: Evaluate the Model Performance
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

r2 = r2_score(y_test, y_pred)
print("R-squared Score:", r2)

# Step 7: Advanced - Model Evaluation and Analysis
comparison_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nComparison of Actual and Predicted Prices:\n", comparison_df.head())

# Step 8: Visualization (Optional)
import matplotlib.pyplot as mplt

plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred, alpha=0.6, color='b')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted House Prices')
plt.show()

