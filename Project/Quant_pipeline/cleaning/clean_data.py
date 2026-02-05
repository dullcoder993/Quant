import pandas as pd

def clean_price_data(df):
    # 1. Sort by date
    df = df.sort_values("date")

    # 2. Set date as index (required for time logic)
    df = df.set_index("date")

    # 3. Create continuous business-day index
    full_index = pd.date_range(
        start=df.index.min(),
        end=df.index.max(),
        freq="B"  # Business days only
    )

    # 4. Reindex to include missing days
    df = df.reindex(full_index)

    # 5. Forward-fill prices (markets don’t jump randomly)
    price_cols = ["open", "high", "low", "close", "adj_close"]
    df[price_cols] = df[price_cols].ffill()

    # 6. Volume should be zero on non-trading days
    df["volume"] = df["volume"].fillna(0)

    # 7. Restore date column
    df = df.reset_index().rename(columns={"index": "date"})
    df.index.name = None
    return df
