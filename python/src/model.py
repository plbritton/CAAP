class Company:
    def __init__(self, name: str, symbol: str, CIK: str):
        self.name = name
        self.symbol = symbol
        self.CIK = CIK


headers = {"User-Agent": "Univ. of Memphis Capstone Project",
           "Accept-Encoding": "gzip",
           "Host": "www.sec.gov"}

link = ""
