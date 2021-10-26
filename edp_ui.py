from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class selectionBox(QWidget):
    def __init__(self):
        super(selectionBox, self).__init__()
        self.rows = 0
        self.columns = 0
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.company_attribute_separator = QHBoxLayout()
        self.company_layout = QVBoxLayout()
        self.selectionLabel = QLabel('Fill in your attributes: ', self)
        self.selectionLabel.setFont(QFont('Arial', 11))
        self.selectionLabel.setStyleSheet("font-weight: bold; color: #3C404D")
        self.selectionLabel.setFixedHeight(100)
        self.selectionLabel.setAlignment(Qt.AlignHCenter)
        self.main_layout.addWidget(self.selectionLabel)
        self.make_row()
        self.make_row()
        self.main_layout.addLayout(self.company_attribute_separator)
        self.company_attribute_separator.addLayout(self.company_layout)
        self.make_attribute_selector()

        self.addRow = QPushButton(self)
        self.addRow.setText("Add Row")
        self.addRow.clicked.connect(self.make_row)
        self.main_layout.addWidget(self.addRow)
        self.addRow.setFixedWidth(200)

        self.submit_button = QPushButton(self)
        self.submit_button.setText("Submit")
        self.submit_button.clicked.connect(self.submit)
        self.main_layout.addWidget(self.submit_button)
        self.submit_button.setFixedWidth(200)

        self.setLayout(self.main_layout)

    def make_row(self, companies = ["Autozone", "Oreilly", "Pepboys"]):
        self.rows += 1
        row_layout = QHBoxLayout()
        row_layout.setAlignment(Qt.AlignLeft)

        #company label
        self.company_label = QLabel(f'Company {self.rows}: ', self)
        self.company_label.setFont(QFont('Arial', 11))
        row_layout.addWidget(self.company_label)

        #company combo box
        self.company_combo = QComboBox(self)
        self.company_combo.setFont(QFont('Arial', 10))
        self.company_combo.setStyleSheet('QComboBox {border: 2px solid gray;}')
        for i in companies:
            self.company_combo.addItem(i)
        self.company_combo.setFixedWidth(200)
        row_layout.addWidget(self.company_combo)

        self.company_layout.addLayout(row_layout)

    def make_attribute_selector(self, attributes = ["Net Profit", "Time"], attribute_count = 2):
        self.attribute_layout = QHBoxLayout()
        self.attribute_layout.setAlignment(Qt.AlignRight)
        self.attribute_layout.addWidget(QLabel("Attributes: "))
        for _ in range(attribute_count):
            attribute_combo = QComboBox(self)
            attribute_combo.setFont(QFont('Arial', 10))
            attribute_combo.setStyleSheet('QComboBox {border: 2px solid gray;}')
            for i in attributes:
                attribute_combo.addItem(i)

            self.attribute_layout.addWidget(attribute_combo)
            attribute_combo.setFixedWidth(200)
        self.company_attribute_separator.addLayout(self.attribute_layout)

    def submit(self):
        QMessageBox.about(self, "Nice!", "You submitted your chart attributes!")


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
        stocks.setVerticalHeaderLabels(["Autozone", "Oreilly", "Pepboiz", "Dr. Yu's very special \nand good auto shop"])
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

        # visualization text settings
        self.visual = QLabel('Select Preferred Chart Visualization:', self)
        self.visual.setFont(QFont('Arial', 12))
        self.visual.setStyleSheet("font-weight: bold; color: #3C404D")
        self.visual.setAlignment(Qt.AlignTop)
        self.main_layout.addWidget(self.visual)

        # visualization drop down box settings
        self.chartSelector = QComboBox(self)
        self.chartSelector.setFont(QFont('Arial', 11))
        self.chartSelector.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.chartSelector.addItem('Bar Graph')
        self.chartSelector.addItem('Line Graph')
        self.chartSelector.addItem('Pie Chart')
        self.chartSelector.addItem('Table')
        self.chartSelector.addItem('Histogram')
        self.chartSelector.addItem('Store Count')
        self.chartSelector.setGeometry(10, 70, 200, 40)

        self.setLayout(self.main_layout)
        attribute_selection = selectionBox()
        self.main_layout.addWidget(attribute_selection)


    #  method for button click function
    def button2_clicked(self):
        QMessageBox.about(self, "Nice!", "You submitted your chart attributes!")


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


# main class
if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())