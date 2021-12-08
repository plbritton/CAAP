from PyQt5.QtWidgets import QWidget, QHBoxLayout

class SelectionBox(QWidget):
    def __init__(self, comp_selector, attrib_selector):
        super().__init__()

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(comp_selector)
        self.layout().addWidget(attrib_selector)
