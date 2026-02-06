import pandas as pd
from sqlalchemy import create_engine

def read_from_postgres(symbol):
    engine = create_engine(
        "postgresql://postgres:Prathu2402@localhost:5432/quantdb"
    )

    query = f"""
    SELECT date, adj_close, close, open
    FROM prices
    WHERE symbol = '{symbol}'
    ORDER BY date
    """

    df = pd.read_sql(query, engine)
    return df