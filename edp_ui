from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


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

        for wid in self.content:
            self.layout.addWidget(wid)

        self.setLayout(self.layout)


class Processor(QWidget):
    def __init__(self):
        super(Processor, self).__init__()
        self.initUI()

    def initUI(self):
        # creates the layouts to place widgets in and format
        self.main_layout = QVBoxLayout()
        self.horiz_layout = QHBoxLayout()
        self.horiz_layout2 = QHBoxLayout()
        self.horiz_layout3 = QHBoxLayout()

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

        # 'fill in attributes' text settings
        self.attrib = QLabel('Fill in your attributes: ', self)
        self.attrib.setFont(QFont('Arial', 11))
        self.attrib.setStyleSheet("font-weight: bold; color: #3C404D")
        self.attrib.setFixedHeight(100)
        self.attrib.setAlignment(Qt.AlignHCenter)
        self.main_layout.addWidget(self.attrib)

        # attribute 1, row 1 text settings
        self.attrib11 = QLabel('Company 1: ', self)
        self.attrib11.setFont(QFont('Arial', 11))
        self.horiz_layout.addWidget(self.attrib11)

        # attribute 1, row 1 drop down box settings
        self.att11 = QComboBox(self)
        self.att11.setFont(QFont('Arial', 10))
        self.att11.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att11.addItem('AutoZone')
        self.att11.addItem("O'Reilly")
        self.att11.addItem('AAP')
        self.horiz_layout.addWidget(self.att11)
        self.att11.setFixedWidth(200)

        # attribute 2, row 1 text settings
        self.plus21 = QLabel(' + ', self)
        self.plus21.setStyleSheet("font-weight: bold; color: black")
        self.horiz_layout.addWidget(self.plus21)
        self.attrib21 = QLabel('Column 1: ', self)
        self.attrib21.setFont(QFont('Arial', 11))
        self.horiz_layout.addWidget(self.attrib21)

        # attribute 2, row 1 drop down box settings
        self.att21 = QComboBox(self)
        self.att21.setFont(QFont('Arial', 10))
        self.att21.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att21.addItem('Net Profit')
        self.att21.addItem("Time")
        self.horiz_layout.addWidget(self.att21)
        self.att21.setFixedWidth(200)

        # attribute 3, row 1 text settings
        self.plus31 = QLabel(' + ', self)
        self.plus31.setStyleSheet("font-weight: bold; color: black")
        self.horiz_layout.addWidget(self.plus31)
        self.attrib31 = QLabel('Column 2: ', self)
        self.attrib31.setFont(QFont('Arial', 11))
        self.horiz_layout.addWidget(self.attrib31)

        # attribute 3, row 1 drop down box settings
        self.att31 = QComboBox(self)
        self.att31.setFont(QFont('Arial', 10))
        self.att31.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att31.addItem('Net Profit')
        self.att31.addItem("Time")
        self.horiz_layout.addWidget(self.att31)
        self.att31.setFixedWidth(200)

        # attribute 1, row 2 text settings
        self.attrib12 = QLabel('Company 2: ', self)
        self.attrib12.setFont(QFont('Arial', 11))
        self.horiz_layout2.addWidget(self.attrib12)

        # attribute 1, row 2 drop down box settings
        self.att12 = QComboBox(self)
        self.att12.setFont(QFont('Arial', 10))
        self.att12.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att12.addItem('AutoZone')
        self.att12.addItem("O'Reilly")
        self.att12.addItem('AAP')
        self.horiz_layout2.addWidget(self.att12)
        self.att12.setFixedWidth(200)

        # attribute 2, row 2 text settings
        self.plus22 = QLabel(' + ', self)
        self.plus22.setStyleSheet("font-weight: bold; color: black")
        self.horiz_layout2.addWidget(self.plus22)
        self.attrib22 = QLabel('Column 1: ', self)
        self.attrib22.setFont(QFont('Arial', 11))
        self.horiz_layout2.addWidget(self.attrib22)


        # attribute 2, row 2 drop down box settings
        self.att22 = QComboBox(self)
        self.att22.setFont(QFont('Arial', 10))
        self.att22.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att22.addItem('Net Profit')
        self.att22.addItem("Time")
        self.horiz_layout2.addWidget(self.att22)
        self.att22.setFixedWidth(200)

        # attribute 3, row 2 text settings
        self.plus32 = QLabel(' + ', self)
        self.plus32.setStyleSheet("font-weight: bold; color: black")
        self.horiz_layout2.addWidget(self.plus32)
        self.attrib32 = QLabel('Column 2: ', self)
        self.attrib32.setFont(QFont('Arial', 11))
        self.horiz_layout2.addWidget(self.attrib32)

        # attribute 3, row 2 drop down box settings
        self.att32 = QComboBox(self)
        self.att32.setFont(QFont('Arial', 10))
        self.att32.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att32.addItem('Net Profit')
        self.att32.addItem("Time")
        self.horiz_layout2.addWidget(self.att32)
        self.att32.setFixedWidth(200)

        # button to add a row of attributes
        self.button1 = QPushButton(self)
        self.button1.setText("Add Another Row + ")
        self.button1.clicked.connect(self.button1_clicked)
        self.horiz_layout3.addWidget(self.button1)
        self.button1.setFixedWidth(300)

        # button to add a row of attributes
        self.button2 = QPushButton(self)
        self.button2.setText("Submit")
        self.button2.clicked.connect(self.button2_clicked)
        self.horiz_layout3.addWidget(self.button2)
        self.button2.setFixedWidth(200)

        # sets alignment for the horizontal layouts
        self.horiz_layout.setAlignment(Qt.AlignHCenter)
        self.horiz_layout2.setAlignment(Qt.AlignHCenter)
        self.horiz_layout3.setAlignment(Qt.AlignHCenter)
        # adds the horizontal layouts into the main vertical layout
        self.main_layout.addLayout(self.horiz_layout)
        self.main_layout.addLayout(self.horiz_layout2)
        self.main_layout.addLayout(self.horiz_layout3)
        # sets the layout
        self.setLayout(self.main_layout)

    # method for button click function
    def button1_clicked(self):
        QMessageBox.about(self, "Nice!", "You added a new row of attributes!")

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