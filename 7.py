# 7. Identify a public API (e.g., OpenWeatherMap, CoinGecko). Use Python to fetch data from the
#  API, store it in a data frame and perform any 5 operations on the data frame.
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch Data from CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',  # Currency to display prices in
    'order': 'market_cap_desc',  # Order by market capitalization (descending)
    'per_page': 10,  # Number of coins to fetch
    'page': 1,  # Page number
    'sparkline': False  # Exclude sparkline data
}

# Make a GET request to the API
response = requests.get(url, params=params)
if response.status_code==200:
    data = response.json()
else:
    print("Error :Unable to fetch data \nStatus code:",response.status_code)
    sys.exit()

# Step 2: Convert JSON data to a Pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df[['id', 'symbol', 'current_price', 'market_cap', 'total_volume']])

# Step 3: Perform Operations on the DataFrame

# 1. Filter cryptocurrencies with price above $10,000
high_value_coins = df[df['current_price'] > 10000]
print("\nCryptocurrencies with Price > $10,000:")
print(high_value_coins[['id', 'current_price']])

# 2. Add a new column for market cap in billions
df['market_cap_billions'] = df['market_cap'] / 1e9
print("\nDataFrame with Market Cap in Billions:")
print(df[['id', 'market_cap', 'market_cap_billions']])

# 3. Sort by total volume traded in descending order
sorted_by_volume = df.sort_values(by='total_volume', ascending=False)
print("\nDataFrame Sorted by Total Volume:")
print(sorted_by_volume[['id', 'total_volume']])

# 4. Calculate the average price of the cryptocurrencies
average_price = df['current_price'].mean()
print(f"\nAverage Price of Cryptocurrencies: ${average_price:.3f}")

# 5. Visualising current price
plt.figure(figsize=(10,5))
plt.plot(df["id"],df["current_price"])
plt.show()
