import pandas as pd
import requests
import numpy as np

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

    def __init__(self, ticker : str, kpi : str, div=None, **kwargs):
        self.company = self.get_company(ticker)
        self.kpi = kpi
        self.form = kwargs.get("form")
        self.years = kwargs.get("years")
        self.div = div
        self.units = None
        self.data = self.get_data(self.company.cik, self.kpi)


        if self.div:
            self.divide(self.div)


    def combine_rows(self, df):
        temp = []
        # pops out first row
        first = df.iloc[0]
        first = pd.DataFrame.from_dict(df.iloc[0]["units"])
        df = df.iloc[1:, :]
        # get the other rows and
        for row in df.iterrows():
            temp.append(row[1].at["units"])
        for dictionary in temp:
            df = first.append(dictionary, ignore_index=True)
        return df

    def get_data(self, cik, kpi):
        # get the json file that contains kpi for a certain company
        d = requests.get(f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{kpi}.json",
                         headers=self.HEADER).json()
        # convert to dataframe
        df = pd.DataFrame.from_dict(d)
        # get the units of the data
        if not self.div:
            self.units = list(d["units"].keys())[-1]
        else:
            pass
        # check to see if you need to combine rows
        if len(df) > 1:
            df = self.combine_rows(df)
        else:
            df = pd.DataFrame.from_dict(d["units"][list(d["units"].keys())[0]])
        # drop irrelevant columns
        df = df.drop(["fy", "accn", "filed", "form", "frame"], axis=1)
        # get the yearly data
        df = df[df["fp"] == "FY"]
        df = df.drop(["fp"], axis=1)
        # convert end dates to datetime object
        end = pd.to_datetime(df["end"])
        df["end"] = end
        # set the index to years
        df.index = df["end"].dt.year
        df.index.rename("Year", inplace=True)
        df.rename(columns={"val": kpi}, inplace=True)
        # drop left over columns
        for column in df.columns:
            if column == "start":
                df = df.drop(["start"], axis=1)
        df = df.drop(["end"], axis=1)
        # takes the max of the yearly data in case their is quarterly data left (this may not always work)
        return df.groupby("Year").max()

    def get_company(self, ticker):
        name = COMPANIES[COMPANIES["Ticker"] == ticker].iloc[0].at["Name"]
        cik = COMPANIES[COMPANIES["Ticker"] == ticker].iloc[0].at["CIK"]
        return Company(name, ticker, cik)

    def divide(self, div):
        self.div = True
        df = self.get_data(self.company.cik, div)
        df = self.data[[self.kpi]].div(df[div], axis=0)
        df = df.dropna()
        df.rename(columns={self.kpi: f"{self.kpi} per {div}"}, inplace=True)
        self.data = df.round(2)

# orly = Report("ORLY", "GrossProfit")
# orly.divide("NumberOfStores")
# print(orly.data)
