from storage.pipeline import ingest_many_stocks

if __name__ == "__main__":
    symbols = [
        "HDFCBANK.NS",
        "RELIANCE.NS",
        "TCS.NS",
        "INFY.NS"
    ]

    results = ingest_many_stocks(symbols, start="2022-01-01")

    for r in results:
        print(r)


