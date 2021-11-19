from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from python.src.model import Report

import random

import sys

#contains company selectors and attribute selectors on the data processing page
class selectionBox(QWidget):
    def __init__(self):
        super(selectionBox, self).__init__()
        self.companies = ["AZO", "ORLY", "PBY"]
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.company_attribute_separator = QHBoxLayout()
        self.company_layout = QVBoxLayout()
        self.attribute_layout = QHBoxLayout()
        self.attribute_layout.addWidget(QLabel("Attributes: "))
        self.company_widgets = []
        self.attribute_widgets = []
        self.selectionLabel = QLabel('Fill in your attributes: ', self)
        self.selectionLabel.setFont(QFont('Arial', 11))
        self.selectionLabel.setStyleSheet("font-weight: bold; color: #3C404D")
        self.selectionLabel.setFixedHeight(100)
        self.selectionLabel.setAlignment(Qt.AlignHCenter)
        self.main_layout.addWidget(self.selectionLabel)
        self.make_row()
        self.main_layout.addLayout(self.company_attribute_separator)
        self.company_attribute_separator.addLayout(self.company_layout)
        self.addRow = QPushButton(self)
        self.addRow.setText("Add Row")
        self.addRow.clicked.connect(self.make_row)
        self.main_layout.addWidget(self.addRow)
        self.addRow.setFixedWidth(200)
        self.setLayout(self.main_layout)

    def make_row(self):
        row_layout = QHBoxLayout()
        row_layout.setAlignment(Qt.AlignLeft)

        #company label
        self.company_label = QLabel(f'Company {len(self.company_widgets)+1}: ', self)
        self.company_label.setFont(QFont('Arial', 11))
        row_layout.addWidget(self.company_label)

        #company combo box
        company_combo = QComboBox(self)
        company_combo.setFont(QFont('Arial', 10))
        company_combo.setStyleSheet('QComboBox {border: 2px solid gray;}')
        for company_name in self.companies:
            company_combo.addItem(company_name)
        company_combo.setFixedWidth(200)
        row_layout.addWidget(company_combo)
        self.company_widgets.append(company_combo)
        self.company_layout.addLayout(row_layout)

    def make_attribute_selector(self, attributes = ["GrossProfit", "NetProfit", "OperatingIncomeLoss"], attribute_count = 3):
        while self.attribute_widgets:
            self.attribute_layout.removeWidget(self.attribute_widgets.pop())
        self.setLayout(self.attribute_layout)
        self.attribute_layout.setAlignment(Qt.AlignRight)
        for _ in range(attribute_count):
            attribute_combo = QComboBox(self)
            attribute_combo.setFont(QFont('Arial', 10))
            attribute_combo.setStyleSheet('QComboBox {border: 2px solid gray;}')
            for selected_attribute in attributes:
                attribute_combo.addItem(selected_attribute)

            self.attribute_layout.addWidget(attribute_combo)
            self.attribute_widgets.append(attribute_combo)
            attribute_combo.setFixedWidth(200)
        perStoreCount = QCheckBox("Per Store?")
        self.attribute_layout.addWidget(perStoreCount)
        self.attribute_widgets.append(perStoreCount)

        self.company_attribute_separator.addLayout(self.attribute_layout)

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


class Processor(QWidget):
    def __init__(self):
        super(Processor, self).__init__()
        self.initUI()

    def initUI(self):
        # creates the layouts to place widgets in and format
        self.main_layout = QVBoxLayout()

        # visualization drop down box settings
        self.chartSelector = QComboBox(self)
        self.chartSelector.setFont(QFont('Arial', 11))
        self.chartSelector.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.chartSelector.addItem('Bar Graph')
        self.chartSelector.addItem('Line Graph')
        self.chartSelector.addItem('Pie Chart')
        self.chartSelector.addItem('Table')
        self.main_layout.addWidget(self.chartSelector)

        # this creates the plot widget
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)
        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.canvas)
        self.main_layout.addWidget(self.button)

        self.chartTypeAttributeCount = {"Bar Graph" : 1, "Line Graph" : 1, "Pie Chart" : 1, "Table" : 1}

        self.setLayout(self.main_layout)
        self.attribute_selection = selectionBox()
        self.modify_attributes()
        self.chartSelector.activated[str].connect(self.modify_attributes)
        self.main_layout.addWidget(self.attribute_selection)

    def plot(self):
        # create reports
        reports = []
        #get all companies shown on EDP page
        for company_selected in self.attribute_selection.company_widgets:
            report = Report(company_selected.currentText(), self.attribute_selection.attribute_widgets[0].currentText())
            if self.attribute_selection.attribute_widgets[-1].isChecked():
                report.divide("NumberOfStores")
            reports.append(report)
        #get all attributes selected on EDP page                            # :-1 excludes the 'per store' button
        for attribute_selected in self.attribute_selection.attribute_widgets[:-1]:
            pass

        # clearing old figure
        self.figure.clear()

        title = self.attribute_selection.attribute_widgets[0].currentText()
        if self.attribute_selection.attribute_widgets[-1].isChecked():
            title += " per Store"

        # create an axis using KPI listed in attribute combo boxes
        ax = self.figure.add_subplot(111, ylabel=self.attribute_selection.attribute_widgets[0].currentText(), title=title)
        # plot data
        for company_data in reports:
            company_data.data.plot(ax=ax)
        ax.legend([company_data.company.name for company_data in reports])

        # refresh canvas
        self.canvas.draw()

    def modify_attributes(self):
        self.attribute_selection.make_attribute_selector(
            attribute_count=self.chartTypeAttributeCount[self.chartSelector.currentText()])


class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        # main window setup
        layout = QVBoxLayout()
        self.setWindowTitle('Competitor Awareness Application (CAAP)')
        self.setLayout(layout)

        dash = Dashboard()
        processor = Processor()

        # tab initialization
        tabwidget = QTabWidget()
        tabwidget.addTab(dash, "Dashboard")
        tabwidget.addTab(processor, "EDGAR Data Processor (EDP)")
        tabwidget.setFont(QFont('Arial', 10))

        layout.addWidget(tabwidget)

        stylesheet = """ 
            QTabBar::tab:selected {background: #9c6879;}
            QTabWidget>QWidget>QWidget{background: #F4f4f4;}
            """

        self.setStyleSheet(stylesheet)

        self.showMaximized()