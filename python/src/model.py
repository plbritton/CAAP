from lxml import etree
import pandas as pd
import edgar
import requests
import ast
from datetime import date

class Company:
    def __init__(self, name: str, symbol: str, cik: str):
        self.name = name
        self.symbol = symbol
        self.cik = cik


class Report:
    # config
    HEADER = {'user-agent': 'University of Memphis'}

    def __init__(self, company : Company, kpi : str, **kwargs):
        self.company = company
        self.kpi = kpi
        self.form = kwargs.get("form")
        self.years = kwargs.get("years")
        self.data = self.get_data()


    def get_data(self):
        d = requests.get(f"https://data.sec.gov/api/xbrl/companyconcept/CIK{self.company.cik}/us-gaap/{self.kpi}.json",
                         headers=self.HEADER).json()
        df = pd.DataFrame.from_dict(d["units"]["USD"])
        df = df.drop(["fy", "frame", "accn", "filed"], axis=1)
        if self.form:
            df = df[df["form"] == f"{self.form}"]
        if self.years:
            df = df[df["start"] == f"{self.years}"]
        return df



# Testing
companies = [Company("Autozone Inc", "AZO", "0000866787"), Company("O REILLY AUTOMOTIVE INC", "ORLY", "0000898173")]

myReport = Report(companies[1], "GrossProfit", form="10-K")
df = myReport.data

start, end = pd.to_datetime(df["start"]), pd.to_datetime(df["end"])
df["start"], df["end"] = start, end
df = df.drop_duplicates()
print(df[df["start"] == "2015-01"] & df["end"] == "2015-12")
