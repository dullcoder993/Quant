import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
def read_from_postgres(symbol):
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")
    engine = create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{db}"
    )

    query = f"""
    SELECT date, adj_close, close, open
    FROM prices
    WHERE symbol = '{symbol}'
    ORDER BY date
    """

    df = pd.read_sql(query, engine)
    return df