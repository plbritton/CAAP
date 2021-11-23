import yfinance as yf

ticker = 'PBY' #PEPBOYS
ticker2 = 'NAPA'
ticker3 = 'AZO'

data = yf.Ticker(ticker)
data2 = yf.Ticker(ticker2)
data3 = yf.Ticker(ticker3)

tFrame = data.history(period = '1d', start = '2021-10-30', end = '2021-11-21')
tFrame2 = data2.history(period = '1d', start = '2021-10-30', end = '2021-11-21')
tFrame3 = data3.history(period = '1d', start = '2021-10-30', end = '2021-11-21')

#displays data
tFrame
tFrame2
tFrame3