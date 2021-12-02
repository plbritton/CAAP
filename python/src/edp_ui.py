from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from python.src.model import Report
import requests
from python.src.config import *
import random
import pandas as pd

import sys


#contains company selectors and attribute selectors on the data processing page
class CompanySelector(QWidget):

    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        #button to add company rows
        addRowButton = QPushButton("Add row")
        addRowButton.setFixedWidth(200)
        addRowButton.clicked.connect(self.makeRow)

        self.layout().addWidget(addRowButton)

        #to track entry boxes
        self.companyRows = []
        self.selectedCompanies = set([])

    def tickerIsValid(self, value):
        if value in allowed_tickers:
            return True
        else:
            return False

    def check_ticker(self):
        #check each row if it is not already grayed out, and if it is not a duplicate of another row
        for entryBox in filter(lambda x : x.text() and x.isEnabled() and x.text().lower() not in self.selectedCompanies, self.companyRows):
            if not self.tickerIsValid(entryBox.text().lower()):
                # throw error message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Ticker not found!')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                #ticker validated, "gray out" to show that the value is set, and add to the list of companies to graph
                entryBox.setDisabled(True)
                self.selectedCompanies.add(entryBox.text().lower())

    # adding a row for a new company
    def makeRow(self):
        row_layout = QHBoxLayout()
        row_layout.setAlignment(Qt.AlignLeft)

        # label the row as "Company #: "
        company_label = QLabel(f"Company {len(self.companyRows) + 1}: ")
        company_label.setAlignment(Qt.AlignLeft)
        row_layout.addWidget(company_label)

        entryBox = QLineEdit(self)
        entryBox.setAlignment(Qt.AlignLeft)
        entryBox.setFixedWidth(100)

        #when enter is pressed, validate all entry boxes
        entryBox.returnPressed.connect(self.check_ticker)
        row_layout.addWidget(entryBox)
        self.companyRows.append(entryBox)

        # add company row to company selector box
        self.layout().addLayout(row_layout)


class AttributeSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignRight)
        self.attributes = []

        label = QLabel("Attributes: ")
        self.layout().addWidget(label)

        self.make_attribute_selector()

    def make_attribute_selector(self, attribute_count = 1):
        #remove current widgets
        while self.attributes:
            self.layout().removeWidget(self.attributes.pop())

        #to label the row

        #depending on the appropriate number of attributes, add selection boxes
        for _ in range(attribute_count):
            attribute_combo = QComboBox(self)
            attribute_combo.setFont(QFont('Arial', 10))
            attribute_combo.setStyleSheet('QComboBox {border: 2px solid gray;}')
            #for each selection box, add all possible KPI's
            for selected_attribute in preferred_KPIs:
                attribute_combo.addItem(selected_attribute)

            attribute_combo.setFixedWidth(200)
            self.layout().addWidget(attribute_combo)
            self.attributes.append(attribute_combo)

        self.perStoreCount = QCheckBox("Per Store?")
        self.layout().addWidget(self.perStoreCount)

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


class SelectionBox2(QWidget):
    def __init__(self, comp_selector, attrib_selector):
        super().__init__()

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(comp_selector)
        self.layout().addWidget(attrib_selector)

class Processor2(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QVBoxLayout())

        self.plotter = Plotter()
        self.companySelector = CompanySelector()
        self.attributeSelector = AttributeSelector()

        self.layout().addWidget(self.plotter)
        self.plotter.plotButton.clicked.connect(self.plot)

        #setting up the selection box this way allows the processor to reference company and attribute selectors directly
        self.layout().addWidget(SelectionBox2(self.companySelector, self.attributeSelector))

    def plot(self):
        reports = []
        for company in self.companySelector.companyRows:
            print(company.text())
            print(self.attributeSelector.attributes[0].currentText())
            report = Report(company.text(), self.attributeSelector.attributes[0].currentText())
            print("checking num stores")
            if self.attributeSelector.perStoreCount.isChecked():
                report.divide("NumberOfStores")

            reports.append(report)
        print("about to plot")
        self.plotter.figure.clear()
        title = self.attributeSelector.attributes[0].currentText()
        print("making title")
        if self.attributeSelector.perStoreCount.isChecked():
            title += " Per Store"

        # create an axis using KPI listed in attribute combo boxes
        print("plotting")
        ax = self.plotter.figure.add_subplot(111, ylabel=self.attributeSelector.attributes[0].currentText(), title=title)
        # plot data
        print("going through reports")
        for company_data in reports:
            company_data.data.plot(ax=ax)
        ax.legend([company_data.company.name for company_data in reports])

        # refresh canvas
        self.canvas.draw()


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
        self.tickersTyped = []
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
        self.submit = QPushButton(self)
        self.addRow.setText("Add Row")
        self.submit.setText("Submit")
        self.addRow.clicked.connect(self.checkIfTicker)
        self.submit.clicked.connect(self.Submit)
        # self.addRow.clicked.connect(self.make_row)
        self.main_layout.addWidget(self.addRow)
        self.addRow.setFixedWidth(200)
        self.main_layout.addWidget(self.submit)
        self.submit.setFixedWidth(200)
        self.setLayout(self.main_layout)

    def checkIfTicker(self):
        value = self.tickerBar.text()
        if value in self.d:
            self.ticker = value.upper()
            self.tickersTyped.append(self.ticker)
            self.make_row()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Ticker not found!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return

    def make_row(self):
        self.row_layout = QHBoxLayout()
        self.row_layout.setAlignment(Qt.AlignLeft)

        #company label
        self.company_label = QLabel(f'Company {len(self.company_widgets)+1}: ', self)
        self.company_label.setFont(QFont('Arial', 11))
        self.row_layout.addWidget(self.company_label)
        self.company_label.setFixedWidth(300)

        self.tickerBar = QLineEdit(self)
        self.tickerBar.setFixedWidth(140)
        self.tickerBar.setMaxLength(10)
        self.tickerBar.setFont(QFont("Arial", 10))

        # self.ticker = self.tickerBar.text()
        # self.tickersTyped.append(self.ticker)
        HEADER = {'user-agent': 'Bob'}
        self.d = requests.get(f"https://www.sec.gov/include/ticker.txt",
                              headers=HEADER).text

        self.company_layout.addLayout(self.row_layout)
        self.row_layout.addWidget(self.tickerBar)
        self.company_widgets.append(self.tickerBar)

    def Submit(self):
        value = self.tickerBar.text()
        if value in self.d:
            self.ticker = self.tickerBar.text().upper()
            self.tickersTyped.append(self.ticker)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Ticker not found!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return

    def make_attribute_selector(self, attributes = ["AccountsPayableCurrent", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic", "InventoryFinishedGoods", "NumberOfStores", "ProfitLoss", "Revenues"], attribute_count = 3):
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
        self.main_layout.addWidget(self.chartSelector)
        self.attribute_selection = selectionBox()

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

        self.modify_attributes()
        self.chartSelector.activated[str].connect(self.modify_attributes)
        self.main_layout.addWidget(self.attribute_selection)

    def plot(self):
        # create reports
        reports = []
        reports_data = []
        units = None
        print(self.attribute_selection.tickersTyped)
        #get all companies shown on EDP page
        for ticker in self.attribute_selection.tickersTyped:
            print(ticker)
            report = Report(ticker, self.attribute_selection.attribute_widgets[0].currentText())
            if self.attribute_selection.attribute_widgets[-1].isChecked():
                report.divide("NumberOfStores")
            reports.append(report)
            reports_data.append(report.data)
        #get all attributes selected on EDP page                            # :-1 excludes the 'per store' button
        for attribute_selected in self.attribute_selection.attribute_widgets[:-1]:
            pass
        # get units
        units = reports[0].units
        if self.attribute_selection.attribute_widgets[-1].isChecked():
            units = units + " / per store"

        # clearing old figure
        self.figure.clear()

        title = self.attribute_selection.attribute_widgets[0].currentText()
        if self.attribute_selection.attribute_widgets[-1].isChecked():
            title += " per Store"

        # create an axis using KPI listed in attribute combo boxes
        ax = self.figure.add_subplot(111, ylabel=units, title=title)
        ax.ticklabel_format(axis='both', style='sci')
        combine = pd.concat(reports_data, axis=1)
        if self.chartSelector.currentText() == 'Bar Graph':
            combine.plot.bar(ax=ax)
        elif self.chartSelector.currentText() == 'Line Graph':
            combine.plot(ax=ax)

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

        #testing
        tabwidget.addTab(Processor2(), "Test Company Selector")

        tabwidget.setFont(QFont('Arial', 10))

        layout.addWidget(tabwidget)

        stylesheet = """ 
            QTabBar::tab:selected {background: #9c6879;}
            QTabWidget>QWidget>QWidget{background: #F4f4f4;}
            """

        self.setStyleSheet(stylesheet)

        self.showMaximized()