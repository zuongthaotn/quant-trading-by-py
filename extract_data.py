import pandas as pd
import platform
import os
import numpy as np
import datetime

dateparse = lambda x: datetime.datetime.strptime(x, '%Y%m%d')

path = os.getcwd()
if platform.system() == 'Windows':
    file = path + '\\VNX.csv'
if platform.system() != 'Windows':
    file = path + '/VNX.csv'
amibroker_data = pd.read_csv(path + '/cophieu68/amibroker_all_data.csv', parse_dates=['<DATE>'], date_parser=dateparse)
amibroker_data.columns = ['Ticker', 'date', 'open', 'hight', 'low', 'close', 'volumn']
vnx_csv_data = pd.read_csv(file, usecols=["ticker"])
ticker_ids = np.array(vnx_csv_data)
for ticker in ticker_ids:
    ticker_id = ticker[0]
    newdf = amibroker_data[(amibroker_data.Ticker == "AAA")]
    new_file = path + "/cophieu68/" + ticker_id + ".csv"
    newdf.to_csv(new_file, index=False)
    print(".")