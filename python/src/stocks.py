import yfinance as yf
import matplotlib
import pandas as pd

class Stocks():
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = self.get_data()

    def get_data(self):
        df = yf.download(tickers=self.ticker, period='1d', interval='1m')
        df = df[["Close"]]
        return df


