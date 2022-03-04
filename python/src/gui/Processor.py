from PyQt5.QtWidgets import QWidget, QVBoxLayout
from python.src.model import Report
import pandas as pd
from python.src.gui.Plotter import Plotter
from python.src.gui.CompanySelector import CompanySelector
from python.src.gui.AttributeSelector import AttributeSelector
from python.src.gui.SelectionBox import SelectionBox

class Processor(QWidget):
    def __init__(self):
        super().__init__()

        self.data = None

        self.setLayout(QVBoxLayout())

        self.plotter = Plotter()
        self.companySelector = CompanySelector()
        self.attributeSelector = AttributeSelector()

        self.layout().addWidget(self.plotter)
        self.plotter.plotButton.clicked.connect(self.plot)

        #setting up the selection box this way allows the processor to reference company and attribute selectors directly
        self.layout().addWidget(SelectionBox(self.companySelector, self.attributeSelector))

    def plot(self):
        if self.companySelector.company_validator():
            reports = []
            reports_data = []
            try:
                for company in self.companySelector.companyRows:
                    report = Report(company.text().upper(), self.attributeSelector.attributes[0].currentText())
                    if self.attributeSelector.perStoreCount.isChecked():
                        report.divide("NumberOfStores")
                    reports.append(report)
                    # Here is where data gets processed into the report.
                    # This is the last moment we can alter the data.
                    report.data = report.data.loc[[2009]]
                    reports_data.append(report.data)
                self.plotter.figure.clear()
                title = self.attributeSelector.attributes[0].currentText()
                if self.attributeSelector.perStoreCount.isChecked():
                    title += " Per Store"

                # create an axis using KPI listed in attribute combo boxes
                ax = self.plotter.figure.add_subplot(111, ylabel=self.attributeSelector.attributes[0].currentText(), title=title)
                # plot data
                ax.ticklabel_format(axis='both', style='sci')

                combine = pd.concat(reports_data, axis=1)
                self.data = combine

                if self.plotter.chartSelector.currentText() == 'Bar Graph':
                    combine.plot.bar(ax=ax)
                elif self.plotter.chartSelector.currentText() == 'Line Graph':
                    combine.plot(ax=ax)
                ax.legend([company_data.company.name for company_data in reports])
                # refresh canvas
                self.plotter.canvas.draw()
            except ValueError as err:
                self.plotter.plotErrorLabel.setText("Error: could not retrieve data")
                return
            except IndexError as err:
                self.plotter.plotErrorLabel.setText("Error: could not retrieve data")
                return
            else:
                self.plotter.plotErrorLabel.setText("")
        else:
            self.plotter.figure.clear()
            self.plotter.canvas.draw()
