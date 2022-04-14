from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFormLayout, QComboBox
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

        #Initilization. Sets the first row to be autozone. 
        self.makeRow()
        self.companyRows[0].setCurrentIndex(0)
        self.makeRow()
        self.companyRows[1].setCurrentIndex(1)
        

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

    # Note: This function may not be needed as the input is now a combobox - Prentice
    def check_tickers(self):
        #check inputs to see if they are all valid tickers and return true or false
        for row in self.companyRows:
            print("Made it in checktickers")
            text = row.currentText()
            print("Made it past currenttext")
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
        print("Made it out of checktickers")

    # adding a row for a new company
    def makeRow(self):
        # label the row as "Company #: "
        company_label = QLabel(f"Company {len(self.companyRows) + 1}:")
        company_label.setFont(QFont("Arial", 12))

        # List of copmanies that are supported
        companyList = ["azo", "orly", "aap", "pby"]
        entryBox = QComboBox()
        entryBox.addItems(companyList)
        entryBox.setFixedWidth(100)
        entryBox.setProperty("Valid", False)

        self.rowLayout.addRow(company_label, entryBox)

        self.companyRows.append(entryBox)

    def removeRow(self):
        if self.companyRows:
            self.rowLayout.removeRow(self.companyRows.pop())


