from lxml import etree
import pandas as pd
import edgar
import requests
import ast
from datetime import date

class Company:
    def __init__(self, name: str, symbol: str, CIK: str):
        self.name = name
        self.symbol = symbol
        self.CIK = CIK


class Report:
    # config
    BASE_URL = "https://www.sec.gov/Archives/"
    XBRL = "https://www.sec.gov/ix?doc=/Archives/"
    DOWNLOAD_PATH = "sample_index"
    USER_AGENT = "Univ. of Memphis Capstone Project"
    HEADER = {"User-Agent": USER_AGENT}

    def __init__(self, company : Company, report_name : str, year : int, quarter : int):
        self.company = company
        self.report_name = report_name
        self.year = year
        self.quarter = quarter
        try:
            self.__xml_url = self.__get_report(self.company, self.report_name, self.year, self.quarter)
        except FileNotFoundError as nf:
            self.__update_index(self.year)
            self.__xml_url = self.__get_report(self.company, self.report_name, self.year, self.quarter)

        self.__xml_tree = self.__get_elemtree(self.__xml_url)

    def __update_index(self, year):
        '''
        Updates the index files, which are used to locate the correct report url.

        :return: None
        '''

        edgar.download_index(self.DOWNLOAD_PATH, year, self.USER_AGENT, skip_all_present_except_last = False)

    def __get_report(self, company : Company, report_name : str, year : int, quarter : int):
        '''
        Locates webpage containing the specified report for the given company, year, and quarter

        :param company: A Company object representing the desired company
        :param report_name: The name of the report, i.e. 10-Q, 10-K, etc
        :return: the URL for the report's webpage
        '''

        #convert {year quarter} index to csv and filter out unneeded reports/companies
        try:
            csv = pd.read_csv(f"{self.DOWNLOAD_PATH}\\{year}-QTR{quarter}.tsv", sep = "\t", lineterminator = "\n")
            csv.columns.values[0] = "Items"
            company_report = csv[csv["Items"].str.contains(str(int(company.CIK))) & csv["Items"].str.contains(report_name)]
            filing = company_report["Items"].str.split("|").to_list()[0]
        except IndexError as ie:
            print("That report must not be available :/")

        #finds SEC url for given company report
        for item in filing:
            if "html" in item:
                extension = item[:-1]
        url = self.BASE_URL + extension

        #get webpage
        r = requests.get(url, headers=self.HEADER)
        df = pd.read_html(r.text)
        doc_index = df[0].dropna()
        doc_name = doc_index[doc_index["Description"].str.contains(report_name)]
        doc_name = doc_name["Document"].str.split("|")[0][0]
        final = self.BASE_URL + extension.replace("-","").replace("index.html","") + "/" + doc_name.split()[0][:-4] + "_htm.xml"
        return final

    def __get_elemtree(self, url):
        '''
        Creates and returns an XML Element Tree object

        :param url: the url of an xml document
        :return: an ElementTree object
        '''
        response = requests.get(url, headers=self.HEADER)
        tree = etree.fromstring(response.content)
        return tree

    def kpi(self, kpi_name):
        '''
        Returns the values of a particular kpi

        :param kpi_name: the name of the kpi you are interested in
                        (must be the camel case version of row names i.e. Gross profit becomes GrossProfit)
        :return: the values of the kpi in a list
        '''
        values = []
        for child in self.__xml_tree:
            if kpi_name in child.tag[child.tag.find("}") + 1:]:
                values.append((child.attrib["contextRef"], child.text))
        return values


# Testing
companies = [Company("Autozone Inc", "AZO", "0000866787"), Company("O REILLY AUTOMOTIVE INC", "ORLY", "0000898173")]

myReport = Report(companies[1], "10-Q", 2021, 2)
print(myReport.kpi("GrossProfit"))
