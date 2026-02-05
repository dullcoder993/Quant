from ingestion.fetch_yfinance import fetch_stock
from cleaning.clean_data import clean_price_data
import pandas as pd

df = fetch_stock("HDFCBANK.NS")
clean_df = clean_price_data(df)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
print(clean_df.iloc[20:29])
#print(clean_df.isna().sum())