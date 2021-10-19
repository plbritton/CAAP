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
        # adds the widgets to the layout then implement it to page

        # visualization
        self.visual = QLabel('Select Preferred Chart Visualization:', self)
        self.visual.setFont(QFont('Arial', 10))
        self.visual.setStyleSheet("font-weight: bold; color: #3C404D")
        self.visual.move(10,50)

        # visualization drop down box settings
        self.chartSelector = QComboBox(self)
        self.chartSelector.setFont(QFont('Arial', 10))
        self.chartSelector.setGeometry(20, 100, 0, 0)
        self.chartSelector.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.chartSelector.addItem('Bar Graph')
        self.chartSelector.addItem('Line Graph')
        self.chartSelector.addItem('Pie Chart')
        self.chartSelector.addItem('Table')
        self.chartSelector.addItem('Histogram')
        self.chartSelector.addItem('Store Count')
        self.chartSelector.adjustSize()

        # fill in attributes text settings
        self.attrib = QLabel('Fill in your attributes: ', self)
        self.attrib.setFont(QFont('Arial', 10))
        self.attrib.setStyleSheet("font-weight: bold; color: #3C404D")
        self.attrib.move(0,1300)

        # attribute 1 row 1 settings
        self.attrib1 = QLabel('Company 1: ', self)
        self.attrib1.setFont(QFont('Arial', 10))
        self.attrib1.move(230,1400)

        # attribute 1 row 1 drop down box settings
        self.att1 = QComboBox(self)
        self.att1.setFont(QFont('Arial', 9))
        self.att1.setGeometry(450, 1400, 0, 0)
        self.att1.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att1.addItem('AutoZone')
        self.att1.addItem("O'Reilly")
        self.att1.addItem('AAP')
        self.att1.adjustSize()
        
        # attribute 2 row 1 settings
        self.plus = QLabel(' + ', self)
        self.plus.setStyleSheet("font-weight: bold; color: black")
        self.plus.move(770, 1400)
        self.attrib21 = QLabel('Column 1: ', self)
        self.attrib21.setFont(QFont('Arial', 10))
        self.attrib21.move(1000, 1400)

        # attribute 2 row 1 drop down box settings
        self.att22 = QComboBox(self)
        self.att22.setFont(QFont('Arial', 9))
        self.att22.setGeometry(1200, 1400, 0, 0)
        self.att22.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att22.addItem('Net Profit')
        self.att22.addItem("Time")
        self.att22.adjustSize()

        # attribute 3 row 1 settings
        self.plus = QLabel(' + ', self)
        self.plus.setStyleSheet("font-weight: bold; color: black")
        self.plus.move(1500, 1400)
        self.attrib21 = QLabel('Column 2: ', self)
        self.attrib21.setFont(QFont('Arial', 10))
        self.attrib21.move(1700, 1400)

        # attribute 3 row 1 drop down box settings
        self.att22 = QComboBox(self)
        self.att22.setFont(QFont('Arial', 9))
        self.att22.setGeometry(1900, 1400, 0, 0)
        self.att22.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att22.addItem('Net Profit')
        self.att22.addItem("Time")
        self.att22.adjustSize()

        # attribute 1 row 2 settings
        self.attrib2 = QLabel('Company 2: ', self)
        self.attrib2.setFont(QFont('Arial', 10))
        self.attrib2.move(230,1500)

        # attribute 1 row 2 drop down box settings
        self.att2 = QComboBox(self)
        self.att2.setFont(QFont('Arial', 9))
        self.att2.setGeometry(450, 1500, 0, 0)
        self.att2.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att2.addItem('AutoZone')
        self.att2.addItem("O'Reilly")
        self.att2.addItem('AAP')
        self.att2.adjustSize()

        # attribute 2 row 2 settings
        self.plus = QLabel(' + ', self)
        self.plus.setStyleSheet("font-weight: bold; color: black")
        self.plus.move(770, 1500)
        self.attrib21 = QLabel('Column 1: ', self)
        self.attrib21.setFont(QFont('Arial', 10))
        self.attrib21.move(1000, 1500)

        # attribute 2 row 2 drop down box settings
        self.att22 = QComboBox(self)
        self.att22.setFont(QFont('Arial', 9))
        self.att22.setGeometry(1200, 1500, 0, 0)
        self.att22.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att22.addItem('Net Profit')
        self.att22.addItem("Time")
        self.att22.adjustSize()

        # attribute 3 row 2 settings
        self.plus = QLabel(' + ', self)
        self.plus.setStyleSheet("font-weight: bold; color: black")
        self.plus.move(1500, 1500)
        self.attrib21 = QLabel('Column 2: ', self)
        self.attrib21.setFont(QFont('Arial', 10))
        self.attrib21.move(1700, 1500)

        # attribute 3 row 2 drop down box settings
        self.att22 = QComboBox(self)
        self.att22.setFont(QFont('Arial', 9))
        self.att22.setGeometry(1900, 1500, 0, 0)
        self.att22.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.att22.addItem('Net Profit')
        self.att22.addItem("Time")
        self.att22.adjustSize()

        # button to add a row of attributes
        self.button1 = QPushButton(self)
        self.button1.setText("Add Another Row + ")
        self.button1.move(20, 1850)
        self.button1.clicked.connect(self.button1_clicked)

        # button to add a row of attributes
        self.button2 = QPushButton(self)
        self.button2.setText("Submit")
        self.button2.move(3550, 1850)
        self.button2.clicked.connect(self.button2_clicked)

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
        # self.setFixedWidth(2000)
       # self.setFixedHeight(1500)

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