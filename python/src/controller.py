from python.gui.MainWindow import Window
from python.gui.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    screen = MainWindow()
    screen.show()
    sys.exit(app.exec_())
