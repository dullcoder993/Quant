import pandas as pd
from statergy.moving_average import strategy
data = pd.read_csv(r"C:\Users\Lenovo\Desktop\Quant\Project\Quant_backtester\data\prices.csv",)

data["date"] = pd.to_datetime(data["date"])

data = data.sort_values("date")
data.set_index("date",inplace=True)

signals = strategy(data)
print(signals)
