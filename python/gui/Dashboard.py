from PyQt5.QtWidgets import QWidget, QTableWidget, QHeaderView, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

class Dashboard(QWidget):
    def __init__(self):
        super(Dashboard, self).__init__()
        self.initUI()

    def initUI(self):
        stocks = QTableWidget(self)
        stocks.setColumnCount(2)
        stocks.setRowCount(4)
        stocks.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        stocks.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        stocks.setHorizontalHeaderLabels(["Stock Price", "Stock Change"])
        stocks.setVerticalHeaderLabels(["Autozone", "Oreilly", "Pepboys", "Dr. Yu's \n auto shop"])
        graph = QLabel("Some stuff can go here")
        graph.setMinimumWidth(1000)
        graph.setAlignment(Qt.AlignCenter)

        self.content = []
        self.content.append(stocks)
        self.content.append(graph)

        self.layout = QHBoxLayout(self)

        for widget in self.content:
            self.layout.addWidget(widget)

        self.setLayout(self.layout)