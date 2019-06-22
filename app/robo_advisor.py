# app/robo_advisor.py

import csv
import json
import os

from dotenv import load_dotenv
import requests
import datetime
import time

load_dotenv() #> loads contents of the .env file into the script's environment


#convert to USD (from shopping cart)
def to_usd(my_price):
    return "${0:.2f}".format(my_price)

#
# INFO INPUTS
#

api_key = my_var = os.environ.get("ALPHAVANTAGE_API_KEY")

#input stock ticker - help from friend

while True:
        symbol = input("Please input the stock ticker for your stock: ")
        if not symbol.isalpha():
            print("Please try again. Input the stock ticker (e.g. MSFT) for your stock")
        else:
            data = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&apikey=" + api_key)

            if "Error" in data.text:
                print("OOPS. This is not a valid ticker. Please try again.")
            else:
                break


#symbol = "MSFT" #TODO ask user

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
response = requests.get(request_url)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

#breakpoint()
tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) # TODO: assumes first day is on top, but consider sort for latest day first

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"] #>137.0000

#max of all high prices
#high_prices = [10, 20, 30, 5]
#recent_high = max(high_prices)

#max of all high and low prices
high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[latest_day]["2. high"]
    low_price = tsd[latest_day]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

#
# INFO OUTPUTS
#

# csv-mgmt/write_teams.py

#csv_file_path = "data/prices.csv" # a relative filepath

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]

        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"],
        })
    
import datetime
print("-------------------------")
print("SELECTED SYMBOL: " + symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:")
now = time.strftime("%Y-%m-%d %H:%M:%p") 
print(str(now))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")

#Recommendations - help from a friend
if float(latest_close) >= (recent_high-(0.2*recent_high)):
    print("RECOMMENDATION: Buy")
    print("RECOMMENDATION REASON: Latest closing price is more than than 20 percent below the recent high price - stock may be rising")
else:
    print("RECOMMENDATION: Don't Buy")
    print("RECOMMENDATION REASON: Latest closing price is less than 20 percent below the recent high price - stock may be going down")

#print("RECOMMENDATION: BUY!")
#print("RECOMMENDATION REASON: TODO")

print("-------------------------")
print(f"WRITING DATA TO CSV:{csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


