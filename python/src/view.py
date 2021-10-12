from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Dashboard(QWidget):
    def __init__(self):
        super(Dashboard, self).__init__()
        self.initUI()


    def initUI(self):

        #center text
        self.content = QLabel(self)
        self.content.setText("Dash")
        self.content.setAlignment(Qt.AlignCenter)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.content)
        self.setLayout(self.layout)

class Processor(QWidget):
    def __init__(self):
        super(Processor, self).__init__()
        self.initUI()


    def initUI(self):

        self.content = QLabel(self)
        self.content.setText("Processor")
        self.content.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.content)
        self.layout.addWidget(self.content)
        self.setLayout(self.layout)

        self.chartSelector = QComboBox(self)
        self.chartSelector.setMaximumWidth(300)
        self.chartSelector.setStyleSheet('QComboBox {border: 2px solid gray;}')
        self.chartSelector.addItem('One')
        self.chartSelector.addItem('Two')
        self.chartSelector.addItem('Three')
        self.chartSelector.addItem('Four')


class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        # main window setup
        layout = QVBoxLayout()
        self.setWindowTitle('Competitor Awareness Application (CAAP)')
        self.setLayout(layout)
        self.setFixedWidth(1000)
        self.setFixedHeight(1000)

        dash = Dashboard()
        processor = Processor()

        # tab initialization
        tabwidget = QTabWidget()
        tabwidget.addTab(dash, "Dashboard")
        tabwidget.addTab(processor, "EDGAR Data Processor (EDP)")

        layout.addWidget(tabwidget)

        self.show()


# main class
if __name__ == "__main__":

    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())