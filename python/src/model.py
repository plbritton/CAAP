import pandas as pd
import requests
import numpy as np
import seaborn as sb

COMPANIES = pd.DataFrame(np.array([["AZO", "Autozone Inc", "0000866787"],
                                   ["ORLY", "O Reilly Automotive Inc", "0000898173"]]),
                         columns=["Ticker", "Name", "CIK"])

class Company:
    def __init__(self, name: str, ticker: str, cik: str):
        self.name = name
        self.ticker = ticker
        self.cik = cik


class Report:
    # config
    HEADER = {'user-agent': 'University of Memphis'}

    def __init__(self, ticker : str, kpi : str, **kwargs):
        self.company = self.get_company(ticker)
        self.kpi = kpi
        self.form = kwargs.get("form")
        self.years = kwargs.get("years")
        self.data = self.get_data()


    def get_data(self):
        d = requests.get(f"https://data.sec.gov/api/xbrl/companyconcept/CIK{self.company.cik}/us-gaap/{self.kpi}.json",
                         headers=self.HEADER).json()
        df = pd.DataFrame.from_dict(d["units"]["USD"])
        df = df.drop(["fy", "accn", "filed", "form"], axis=1)
        df = df[df["frame"].str.contains("Q") == False]
        df = df.drop(["frame", "fp"], axis=1)
        start, end = pd.to_datetime(df["start"]), pd.to_datetime(df["end"])
        df["start"], df["end"] = start, end
        # df = df[(df["start"].dt.month == 1) & (df["end"].dt.month == 12)]

        df.index = df["start"].dt.year
        df.index.rename("Year", inplace=True)
        df.rename(columns={"val": self.kpi}, inplace=True)
        df = df.drop(["start", "end"], axis=1)
        if self.form:
            df = df[df["form"] == f"{self.form}"]
        if self.years:
            df = df[(df["start"] >= f"{self.years[0]}-01-01") & (df["end"] <= f"{self.years[1]}-12-31") & (df["end"].dt.month == 12) & (df["start"].dt.month == 1)]
        df = df.drop_duplicates()
        return df

    def get_company(self, ticker):
        name = COMPANIES[COMPANIES["Ticker"] == ticker].iloc[0].at["Name"]
        cik = COMPANIES[COMPANIES["Ticker"] == ticker].iloc[0].at["CIK"]
        return Company(name, ticker, cik)








