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

latest_close = parsed_response["Time Series (Daily)"]["2019-06-21"]["4. close"] #>137.0000

#breakpoint()



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
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")