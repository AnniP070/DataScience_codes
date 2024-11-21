#6.  Identify a website with tabular data (e.g., a Wikipedia table). Use BeautifulSoup to scrape the data, store it in a Data Frame and perform any 5 operations on the data frame.
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Scrape data
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'
# Get webpage content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
    
# Find first table
table = soup.find('table')
    
# Use pandas to read the HTML table
df = pd.read_html(str(table))[0]

# Operation 1: Display basic info
print("DataFrame Info:")
print(df.info())

# Operation 2: Filter rows based on condition
print("\nTop 5 companies:")
print(df.head())

# Operation 3: Check for missing values
print("\nMissing Data:")
print(df.isnull().sum())

# Operation 4: Drop missing values column
print("\Dropped Data:")
df.drop("State-owned",axis=1, inplace=True)
print(df.head())

# Operation 5: Column-wise summary
print("\nColumn-wise Data Types:")
print(df.dtypes)
