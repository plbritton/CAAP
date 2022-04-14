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
                    report = Report(company.currentText().upper(), self.attributeSelector.attributes[0].currentText())
                    if self.attributeSelector.perStoreCount.isChecked():
                        report.divide("NumberOfStores")
                    reports.append(report)
                    # Here is where data gets processed into the report.
                    # This is the last moment we can alter the data.
                    reports_data.append(report.data)
                #Filtering the data by a specific year. If no, will list every year.
                
                #Note that these prompts to the users will eventually be replaced by GUI elements
                #Where instead, the program will look at that gui element and just pull that data.
                '''yearselect = input("Filter by year? y/n: ")
                if (yearselect == "y"):
                    # This prompt is to be replaced with pulling from the GUI. 
                    yearselect2 = input("Range? y/n: ")
                    # Filtering by a range of years.
                    if (yearselect2 == "y"):
                        # These prompts are to be replaced with pulling from the GUI.
                        lowerrange = int(input("Lower Range of years: "))
                        upperrange = int(input("Upper Range of years: "))
                        for i in range(len(reports_data)):
                            reports_data[i] = reports_data[i].loc[lowerrange:upperrange, :]
                    # Filtering by a specific year. 
                    else:
                        # This prompt is to be replaced with pulling from the GUI.
                        yearselect3 = int(input("What year: "))
                        for i in range(len(reports_data)):
                            reports_data[i] = reports_data[i].loc[[yearselect3]]
                        '''

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
