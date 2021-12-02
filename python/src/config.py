import requests
HEADER = {'user-agent': 'Capstone Project'}
allowed_tickers = requests.get(f"https://www.sec.gov/include/ticker.txt", headers=HEADER).text
preferred_KPIs = ["AccountsPayableCurrent", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic", "InventoryFinishedGoods", "NumberOfStores", "ProfitLoss", "Revenues"]
chart_types = ["Bar Graph", "Line Graph"]