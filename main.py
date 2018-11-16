import statsmodels.tsa.stattools as smt
import pandas as pd
from utils import *

""" Read 2 csv files and calculate percent changes in data """
prices = pd.read_csv('btc_price.csv', header=None, names=['date', 'price'])
prices = refactor_series(prices, 'price')
trade_volume = pd.read_csv("trade-volume.csv", header=None, names=['date', 'volume'])
trade_volume = refactor_series(trade_volume, 'volume')

bigdata = prices.set_index('date').join(trade_volume.set_index('date'), lsuffix='_prices', rsuffix='_volume')

""" Print results of granger causality test and data plot """
plot2ax(bigdata, 'change_percent_prices', 'change_percent_volume')

np_arr = bigdata[['change_percent_prices', 'change_percent_volume']].values
print(smt.grangercausalitytests(np_arr[360:], 3))
