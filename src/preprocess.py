import os
import sys
import pandas as pd
import sqlite3

sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
from src import config

def preprocess_data():

    # Will transform original raw data to optimize selected model processing

    # Connect to the database
    conn = sqlite3.connect(config.DATABASE_PATH)

    # Read a table into a Pandas DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {config.RAW_TABLE}", conn)

    # Apply preprocessing

    # Commit to save preprocessed data to db table and close the connection
    conn.commit()
    conn.close()

    # DBG # Log completion to console
    print(f'Lorem ipsum dolor in {config.PROCESSED_TABLE} table.')