# app/robo_advisor.py

import requests
import json
import datetime
import time

#convert to USD (from shopping cart)
def to_usd(my_price):
    return "${0:.2f}".format(my_price)

#
# INFO INPUTS
#

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
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

#max of all high prices
high_prices = []

for date in dates:
    high_price = tsd[latest_day]["2. high"]
    high_prices.append(float(high_price))

recent_high = max(high_prices)



#
# INFO OUTPUTS
#
import datetime
print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:")
now = time.strftime("%Y-%m-%d %H:%M:%p") 
print(str(now))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")