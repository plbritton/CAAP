import pandas as pd
import edgar
from datetime import date
class Company:
    def __init__(self, name: str, symbol: str, CIK: str):
        self.name = name
        self.symbol = symbol
        self.CIK = CIK

autozone = Company("Autozone Inc", "AZO", "0000866787")

download_path = "C:\\Users\\canon\\PycharmProjects\\CAAP\\sample_index"
base_url = "https://www.sec.gov/Archives/"
#pulling index file from EDGAR
edgar.download_index(download_path, 2018, "Univ. of Memphis Capstone Project", skip_all_present_except_last = False)

companies = ["AUTOZONE INC", "O REILLY AUTOMOTIVE INC"]
desired_report = "10-Q"

#convert 2019 Quarter 4 index to csv
csv = pd.read_csv(f"{download_path}\\2019-QTR4.tsv", sep = "\t", lineterminator = "\n")

csv.columns.values[0] = "Items"
reports = []

#filters out unneeded companies and reports
for c in companies:

    company_report = csv[csv["Items"].str.contains(c) & csv["Items"].str.contains(desired_report)]

    filing = company_report["Items"].str.split("|").to_list()

    #finds SEC url for given company
    for item in filing[0]:
        if "html" in item:
            reports.append(item[:-1])

#add urls to base url
urls = list(map(lambda x : base_url+x, reports))
print(urls)

df = pd.read_html(urls[0])
doc_index = df[0].dropna()

#provides url
doc_name = doc_index[doc_index["Description"].str.contains(desired_report)]
doc_name = doc_name["Document"].str.split("|")
doc_name = doc_name[0][0]

final = reports[0].replace("-","".replace("index.html",""))
print(final)