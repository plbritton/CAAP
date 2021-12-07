from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QLineEdit, QLabel, QFormLayout, QGroupBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from python.src.config import *


class CompanySelector(QWidget):

    def __init__(self):
        super().__init__()
        #to track entry boxes
        self.companyRows = []
        self.selectedCompanies = set([])

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.formLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.formLayout)
        self.rowLayout = QFormLayout()
        self.formLayout.addLayout(self.rowLayout)

        self.buttonLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.buttonLayout)

        #button to add company rows
        addRowButton = QPushButton("Add row")
        addRowButton.setFixedWidth(200)
        addRowButton.clicked.connect(self.makeRow)
        self.buttonLayout.addWidget(addRowButton)

        # button to remove company rows
        removeRowButton = QPushButton("Remove row")
        removeRowButton.setFixedWidth(200)
        removeRowButton.clicked.connect(self.removeRow)
        self.buttonLayout.addWidget(removeRowButton)

        self.makeRow()

    def company_validator(self):
        valid = True
        self.check_tickers()
        for row in self.companyRows:
            if not row.property("Valid"):
                valid = False
        return valid


    def tickerIsValid(self, value):
        if value in allowed_tickers:
            return True
        else:
            return False

    def check_tickers(self):
        #check inputs to see if they are all valid tickers and return true or false
        for row in self.companyRows:
            text = row.text()
            if bool(text) and self.tickerIsValid(text):
                if not row.property("Valid"):
                    row.setProperty("Valid", True)
                    label = self.rowLayout.labelForField(row)
                    label.setStyleSheet("")
                self.selectedCompanies.add(text)
            else:
                row.setProperty("Valid", False)
                label = self.rowLayout.labelForField(row)
                label.setStyleSheet("color: red")

    # adding a row for a new company
    def makeRow(self):
        # label the row as "Company #: "
        company_label = QLabel(f"Company {len(self.companyRows) + 1}:")
        company_label.setFont(QFont("Arial", 12))

        entryBox = QLineEdit()
        entryBox.setFixedWidth(100)
        entryBox.setProperty("Valid", False)

        self.rowLayout.addRow(company_label, entryBox)

        self.companyRows.append(entryBox)

    def removeRow(self):
        if self.companyRows:
            self.rowLayout.removeRow(self.companyRows.pop())


