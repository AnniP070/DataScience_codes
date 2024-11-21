# 13. Perform a hypothesis test to determine if the mean of a sample differs significantly from a known population mean.
############################################  PART 1  #######################################################
import pandas as pd
from scipy import stats
import numpy as np

# Load the iris dataset
df = pd.read_csv("iris.csv")

# Known population mean for 'SepalLengthCm'
population_mean = 5.0

# Sample data: Sepal Length from the Iris dataset
sample_data = df['SepalLengthCm']

# Perform a one-sample t-test
t_stat, p_value = stats.ttest_1samp(sample_data, population_mean)

# Output the results
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Define the significance level (alpha)
alpha = 0.05  # 5% significance level

# Determine if we reject the null hypothesis
if p_value < alpha:
    print("Reject the null hypothesis: The sample mean is significantly different from the population mean.")
else:
    print("Fail to reject the null hypothesis: The sample mean is not significantly different from the population mean.")


############################################  PART 2  #######################################################
# Sample data
print("\n\n")
sample_data = [98, 102, 101, 99, 97]

# Known population mean
population_mean = 100

# Calculate sample mean and sample standard deviation
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data, ddof=1)  # Use ddof=1 for sample standard deviation

# Perform the one-sample t-test
t_statistic, p_value = stats.ttest_1samp(sample_data, population_mean)

# Output results in a simple way
print("Sample Mean:", sample_mean)
print("Sample Standard Deviation:", sample_std)
print("T-Statistic:", t_statistic)
print("P-Value:", p_value)

# Determine significance level
alpha = 0.05

if p_value / 2 < alpha:  # Divide p-value by 2 for a two-tailed test
    print("Reject the null hypothesis: There is a significant difference.")
else:
    print("Fail to reject the null hypothesis: No significant difference.")
