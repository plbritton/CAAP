from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from python.src.config import *

class Plotter(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)

        self.chartSelector = QComboBox(self)
        self.chartSelector.setFont(QFont("Arial", 11))

        for chartType in chart_types:
            self.chartSelector.addItem(chartType)

        self.layout().addWidget(self.chartSelector)

        #actual plot
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.plotButton = QPushButton('Plot')

        self.layout().addWidget(self.toolbar)
        self.layout().addWidget(self.canvas)
        self.layout().addWidget(self.plotButton)