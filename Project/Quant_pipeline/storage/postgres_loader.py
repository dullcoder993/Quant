import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
 
load_dotenv()

def load_to_postgres(df):
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")
    engine = create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{db}"
    )

    df.to_sql(
        "prices",
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )
