from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QMenuBar, QMainWindow, QAction, QMenu, QFileDialog
from python.src.gui.Dashboard import Dashboard
from python.src.gui.Processor import Processor
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Competitor Awareness Application (CAAP)')

        self._createActions()
        self._createMenuBar()
        self.window = Window()
        self.setCentralWidget(self.window)

        self.showMaximized()

    def _createMenuBar(self):
        menuBar = self.menuBar()
        # File menu
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.exportActionExcel)
        fileMenu.addAction(self.exportActionCSV)

    def _createActions(self):
        self.exportActionExcel = QAction("&Export to Excel", self)
        self.exportActionExcel.triggered.connect(self.exportExcel)
        self.exportActionCSV = QAction("&Export to CSV", self)
        self.exportActionCSV.triggered.connect(self.exportCSV)

    def exportExcel(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
        df = self.window.processor.data.copy(deep=True)
        try:
            df = df.astype(object)
            df.to_excel(name[0])
            print("Data export completed")
            return
        # This exception is when the user enters the file as anything but an xlsx file. 
        except ValueError:
            print("File must be saved as a .xlsx file.")
            return
            
        except Exception:
            print("No data to save")
            return

    def exportCSV(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
        df = self.window.processor.data.copy(deep=True)
        try:
            df = df.astype(object)
            df.to_csv(name[0])
            print("Data export completed")
            return
        # This exception is when the user enters the file as anything but a csv file. 
        except ValueError:
            print("File must be saved as a .csv file.")
            return
            
        except Exception:
            print("No data to save")
            return





class Window(QWidget):

    def __init__(self):
        super().__init__()
        # main window setup
        layout = QVBoxLayout()
        self.setLayout(layout)

        menu_bar = QMenuBar()

        self.dash = Dashboard()
        self.processor = Processor()

        # tab initialization
        tabwidget = QTabWidget()
        tabwidget.addTab(self.dash, "Dashboard")
        tabwidget.addTab(self.processor, "EDGAR Data Processor (EDP)")

        layout.addWidget(tabwidget)

