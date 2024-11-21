# 3.Create a data frame from a dictionary of lists. Perform basic operations like selecting rows/columns, filtering, and sorting.
import pandas as pd
data = {
    'Name': ['Avi', 'Jay', 'Pran'],
    'Age': [29, 28, 24],
    'Country': ['Junnar', 'Lonar', 'Murbad']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

ages = df['Age']
print("\nAges Column:")
print(ages) #selecting column

name_country = df[['Name', 'Country']]
print("\nName and Country Columns:")
print(name_country)

first_row = df.iloc[0]
print("\nFirst Row (using iloc):")
print(first_row) # only integer 

first_two_rows = df.loc[0:3]
print("\nFirst Two Rows (using loc):")
print(first_two_rows) # integer and conditions

older_than_25 = df[df['Age'] > 25]
print("\nIndividuals Older Than 25:")
print(older_than_25) #filtering

sorted_df = df.sort_values(by='Age',ascending=False)
print("\nDataFrame Sorted by Age:")
print(sorted_df) #sorting
