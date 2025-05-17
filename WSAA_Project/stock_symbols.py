"""
---------------------------------------------------------------
Fetching stock symbols from Yahoo Finance
---------------------------------------------------------------
Author: Ebelechukwu Igwagu
---------------------------------------------------------------
This script fetches stock symbols from Yahoo Finance and saves them to a JSON file.
"""

import requests
import json
import time
import os

# Soecifies the file path to save the JSON data
file_path = r"C:\Users\great\Desktop\ATU\Year 2\Sem 1\web services and applications\WSAA-coursework\WSAA_Project/stock_symbols.json"

# Yahoo Finance Screener Endpoint
url = "https://query1.finance.yahoo.com/v1/finance/screener/predefined/saved?scrIds=most_actives&count=50"

time.sleep(2)  # Adding a delay 

try:
    # Adding headers to mimic a browser request to avoid being blocked by the server
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    # Get the data from Yahoo Finance WITH headers
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an HTTPError if the response was an error

    data = response.json()

    # Save the data to a JSON file
    with open(file_path, "w") as st:
        json.dump(data, st, indent=4)

    #print("Stock data saved to stock_symbols.json")

except requests.RequestException as e:
    print(f"Error fetching stock data: {e}")

# Extracting the stock symbols from the JSON data
stocks = data["finance"]["result"][0]["quotes"]
for stock in stocks:
    symbol = stock.get("symbol")
    display_name = stock.get("displayName")
    longName = stock.get("longName")
    print(f"{symbol}, {display_name}, {longName}")
