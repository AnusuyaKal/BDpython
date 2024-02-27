import requests
import json
# Function to get live stock data for a symbol
def get_stock_data():
	url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
	response = requests.get(url)
	print(response)
	
	# Check if the response is successful
	if response.status_code == 200:
		data = response.json()
		print(data)
		last_refreshed = data["Meta Data"]["3. Last Refreshed"]
		price = data["Time Series (5min)"][last_refreshed]["1. open"]
		return price
	else:
		return None

stock_prices = {}
price = get_stock_data()
symbol="IBM"
if price is not None:
	stock_prices[symbol] = price

print(f"{symbol}: {price}")



# Alternatively, you can save the data to a file
# with open('quotes.txt', 'w') as f:
#     for i in range(len(quotes)):
#         f.write("Quote: " + quotes[i].text + "\n")
#         f.write("Author: " + authors[i].text + "\n\n")
