import numpy as np
import pandas as pd
import Ticker
import platform
import os

# vnx = pd.read_csv('data/VNX.csv', usecols=["ticker", "exchange"])
# vnx_ticker = np.array(vnx)
vnx_ticker = Ticker.getListVN30ProfitableOfStockBreakout()
total_buy = 0
total_sell = 0
os.chdir('../')
path = os.getcwd()
for ticker in vnx_ticker:
    # ticker_id = ticker[0]
    ticker_id = ticker
    # ticker_exchange = ticker[1]
    # if ticker_exchange == 'HOSE':
    if platform.system() == 'Windows':
        file = path + '\\cophieu68\\' + ticker_id + '.csv'
    if platform.system() != 'Windows':
        file = path + '/cophieu68/' + ticker_id + '.csv'
    ticker_data = pd.read_csv(file, usecols=["Close"])
    price = np.array(ticker_data["Close"])
    # reversed_price = price[::-1]  # Reverse an array
    if Ticker.isStockOut(price):
        print("Mua co phieu " + ticker_id + " voi gia " + str(price[-1]))