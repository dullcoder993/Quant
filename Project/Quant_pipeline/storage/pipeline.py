from ingestion.fetch_yfinance import fetch_stock
from storage.postgres_loader import load_to_postgres
from cleaning.clean_data import clean_price_data
import numpy as np

def ingest_stock_to_db(symbol, start, end):
    # 1. Fetch
    raw_df = fetch_stock(symbol, start=start, end=end)

    # 2. Clean
    clean_df = clean_price_data(raw_df)

    # 3. Add Log Return (Feature Engineering Step)
    clean_df["log_return"] = np.log(
        clean_df["adj_close"] / clean_df["adj_close"].shift(1)
        )

    # First row per symbol → no previous price
    clean_df["log_return"] = clean_df["log_return"].fillna(0)

    # 4. Safety check
    assert clean_df.isna().sum().sum() == 0, "NaNs found after cleaning"

    # 5. Load
    load_to_postgres(clean_df)

    return f"{symbol} ingested successfully"

def ingest_many_stocks(symbols, start,end):
    results = []

    for symbol in symbols:
        try:
            msg = ingest_stock_to_db(symbol, start=start,end = end)
            results.append(msg)
        except Exception as e:
            results.append(f"{symbol} failed: {e}")

    return results