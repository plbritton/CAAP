from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QMessageBox, QLineEdit, QComboBox, QCheckBox
from PyQt5.QtCore import Qt
from python.src.config import *

class SelectionBox(QWidget):
    def __init__(self, comp_selector, attrib_selector):
        super().__init__()

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(comp_selector)
        self.layout().addWidget(attrib_selector)
