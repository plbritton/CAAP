from lxml import etree
import pandas as pd
import edgar
import requests
from datetime import date

class Company:
    def __init__(self, name: str, symbol: str, CIK: str):
        self.name = name
        self.symbol = symbol
        self.CIK = CIK

autozone = Company("Autozone Inc", "AZO", "0000866787")

#CONFIG
BASE_URL = "https://www.sec.gov/Archives/"
XBRL = "https://www.sec.gov/ix?doc=/Archives/"
companies = [Company("Autozone Inc", "AZO", "0000866787"), Company("O REILLY AUTOMOTIVE INC", "ORLY", "0000898173")]
DOWNLOAD_PATH = "sample_index"
USER_AGENT = "Univ. of Memphis Capstone Project"
HEADER = {"User-Agent":USER_AGENT}

def update_index():
    '''
    Updates the index files, which are used to locate the correct report url.

    :return: None
    '''

    edgar.download_index(DOWNLOAD_PATH, 2018, USER_AGENT, skip_all_present_except_last = False)

def get_report(company : Company, report_name : str, year = date.today().year-1, quarter = 1):
    '''
    Locates webpage containing the specified report for the given company, year, and quarter

    :param company: A Company object representing the desired company
    :param report_name: The name of the report, i.e. 10-Q, 10-K, etc
    :return: the URL for the report's webpage
    '''

    #convert {year quarter} index to csv and filter out unneeded reports/companies
    try:
        csv = pd.read_csv(f"{DOWNLOAD_PATH}\\{year}-QTR{quarter}.tsv", sep = "\t", lineterminator = "\n")
        csv.columns.values[0] = "Items"
        company_report = csv[csv["Items"].str.contains(str(int(company.CIK))) & csv["Items"].str.contains(report_name)]
        filing = company_report["Items"].str.split("|").to_list()[0]
    except IndexError as ie:
        print("That report must not be available :/")

    #finds SEC url for given company report
    for item in filing:
        if "html" in item:
            extension = item[:-1]
    url = BASE_URL + extension

    #get webpage
    r = requests.get(url, headers=HEADER)
    df = pd.read_html(r.text)
    doc_index = df[0].dropna()
    doc_name = doc_index[doc_index["Description"].str.contains(report_name)]
    doc_name = doc_name["Document"].str.split("|")[0][0]
    final = BASE_URL + extension.replace("-","").replace("index.html","") + "/" + doc_name.split()[0][:-4] + "_htm.xml"
    return final

def get_elemtree(url):
    '''
    Creates and returns an XML Element Tree object

    :param url: the url of an xml document
    :return: an ElementTree object
    '''
    response = requests.get(url, headers=HEADER)
    tree = etree.fromstring(response.content)
    return tree

xml = get_report(companies[1],"10-Q",2021,2)
tree = get_elemtree(xml)

