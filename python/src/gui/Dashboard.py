from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from python.src.stocks import Stocks
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from python.src.gui.News import News



class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QHBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.plotLayout = QVBoxLayout(self)
        self.mainLayout.addLayout(self.plotLayout)

        self.add_stocks_plot("azo")
        self.add_stocks_plot("orly")
        self.add_stocks_plot("napa")

        self.mainLayout.addWidget(News())


    def add_stocks_plot(self, ticker):
        figure = plt.figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111, title=ticker.upper() + " Stocks")
        stocks = Stocks(ticker)
        stocks.data.plot(ax=ax, legend=False)

        self.plotLayout.addWidget(canvas)
