from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QCheckBox
from PyQt5.QtCore import Qt
from python.src.config import *

class AttributeSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignRight)
        self.attributes = []

        label = QLabel("Attributes: ")
        label.setFont(QFont("Arial", 12))
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