import ccxt
import pandas as pd
import time
import os
from dotenv import load_dotenv

load_dotenv()

bybit_api_key = os.getenv('bybit_api_key')
bybit_api_secret = os.getenv('bybit_api_secret')

bybit = ccxt.bybit({
    'apiKey': bybit_api_key,
    'secret': bybit_api_secret,
})


def fetchFundingRate(exchange, symbol):
    ticker = exchange.fetch_ticker(symbol)
    return float(ticker['info']['fundingRate'])

symbol = 'BTCUSDT'

# Fetch all perpetual contracts
funding_rate = fetchFundingRate(bybit,symbol)

print(f"Funding rate for {symbol}: {funding_rate*100}")

