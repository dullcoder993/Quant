from ingestion.fetch_yfinance import fetch_stock
from storage.postgres_loader import load_to_postgres
from cleaning.clean_data import clean_price_data

def ingest_stock_to_db(symbol, start="2026-01-01"):
    # 1. Fetch
    raw_df = fetch_stock(symbol, start=start)

    # 2. Clean
    clean_df = clean_price_data(raw_df)

    # 3. Safety check
    assert clean_df.isna().sum().sum() == 0, "NaNs found after cleaning"

    # 4. Load
    load_to_postgres(clean_df)

    return f"{symbol} ingested successfully"

def ingest_many_stocks(symbols, start="2022-01-01"):
    results = []

    for symbol in symbols:
        try:
            msg = ingest_stock_to_db(symbol, start=start)
            results.append(msg)
        except Exception as e:
            results.append(f"{symbol} failed: {e}")

    return results