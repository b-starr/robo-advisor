# Robo Advisor

This program asks for an input of a stock ticker, provides current data, and makes a suggestion for Buy or Don't Buy. Using data from the Alpha Advantage API.

## Prerequisites

  Python 3.7
  Anaconda 3.7

Program will: 
import csv
import json
import os

from dotenv import load_dotenv
import requests
import datetime
import time
  
## Installing

Fork the Project Repository [here](https://github.com/prof-rossetti/nyu-info-2335-201905/tree/master/projects/robo-advisor). Clone and download to your computer.

Create a new virtual environment with anaconda called stocks-env

Please obtain an AlphaVantage API Key [here](https://www.alphavantage.co/support/#api-key) 
Once obtained, update the ".env" file with your API Key.

## Run the Program  

Run the program from the command line by typing:

```py
python app/robo_advisor.py
```