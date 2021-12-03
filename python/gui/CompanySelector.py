from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QLineEdit, QLabel
from PyQt5.QtCore import Qt
from python.src.config import *


class CompanySelector(QWidget):

    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        #button to add company rows
        addRowButton = QPushButton("Add row")
        addRowButton.setFixedWidth(200)
        addRowButton.clicked.connect(self.makeRow)

        self.layout().addWidget(addRowButton)

        #to track entry boxes
        self.companyRows = []
        self.selectedCompanies = set([])

    def tickerIsValid(self, value):
        if value in allowed_tickers:
            return True
        else:
            return False

    def check_ticker(self):
        #check each row if it is not already grayed out, and if it is not a duplicate of another row
        for entryBox in filter(lambda x : x.text() and x.isEnabled() and x.text().lower() not in self.selectedCompanies, self.companyRows):
            if not self.tickerIsValid(entryBox.text().lower()):
                # throw error message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Ticker not found!')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                #ticker validated, "gray out" to show that the value is set, and add to the list of companies to graph
                entryBox.setDisabled(True)
                self.selectedCompanies.add(entryBox.text().lower())

    # adding a row for a new company
    def makeRow(self):
        row_layout = QHBoxLayout()
        # label the row as "Company #: "
        company_label = QLabel(f"Company {len(self.companyRows) + 1}: ")
        row_layout.addWidget(company_label)

        entryBox = QLineEdit(self)
        entryBox.setFixedWidth(100)
        #when enter is pressed, validate all entry boxes
        entryBox.returnPressed.connect(self.check_ticker)
        row_layout.addWidget(entryBox)
        self.companyRows.append(entryBox)

        # add company row to company selector box
        self.layout().addLayout(row_layout)