from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QMenuBar, QMainWindow, QAction, QMenu, QFileDialog
from python.gui.Dashboard import Dashboard
from python.gui.Processor import Processor
import pandas

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
        fileMenu.addAction(self.exportAction)

    def _createActions(self):
        self.exportAction = QAction("&Export", self)
        self.exportAction.triggered.connect(self.export)

    def export(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
        try:
            self.window.processor.data.to_excel(name)
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

