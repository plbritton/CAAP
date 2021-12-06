import yfinance as yf
import matplotlib
import pandas as pd


d = yf.download(tickers='AZO', period = '1d', interval = '15m')
print('this is AutoZone in realtime')
y = d["High"]
d.plot(y=y)

# d2 = yf.download(tickers='GPC', period = '1d', interval = '15m')
# print('this is NAPA in realtime')
# print(d2)
#
# d3 = yf.download(tickers='PBY', period = '1d', interval = '15m')
# print('this is Pep Boys in realtime')
# print(type(d3))

