import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")
    return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

def read_prices_for_lppl(symbol):
    engine = get_engine()
    
    # Using text() and params for SQL safety
    query = text("""
        SELECT date, adj_close , log_return
        FROM prices 
        WHERE symbol = :symbol 
        ORDER BY date ASC
    """)
    
    # 1. Load data
    df = pd.read_sql(query, engine, params={"symbol": symbol})
    
    if df.empty:
        return None
    
    # 2. Transform for the LPPL Math
    # We create 't' as an ordinal sequence (1, 2, 3...)
    df['t'] = np.arange(len(df))
    
    # 'Logarithmic Turn': Essential for Phase 1 math
    df['log_price'] = np.log(df['adj_close'])
    return df