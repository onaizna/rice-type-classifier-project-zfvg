import sqlite3
import pandas as pd
import sys
import os
import logging

sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
from src import config

def load_data():
    logging.info('Opening Dataset Files...')
    #df = pd.read_excel(os.path.join(config.RAW_DATA_PATH,'rawdataset_name.xlsx'))
    df = pd.read_csv(os.path.join(config.RAW_DATA_PATH,'rawdataset.csv'))
    logging.info('Raw Dataset Files Loaded')

    # Selecting necessary columns from each dataframe
    df = df[['col1', 'col2']]
    
    # Removing duplicates for every dataframe
    df = df.drop_duplicates()

    # Reset df indexes
    df.reset_index(drop=True, inplace=True)
    
    # Create a connection to the SQLite database (or create if it doesn't exist)
    conn = sqlite3.connect(config.DATABASE_PATH)

    # Write the DataFrame to a table (replace 'my_table' with your desired table name)
    df.to_sql(config.RAW_TABLE, conn, if_exists='replace', index=False)

    # Commit and close the connection
    conn.commit()
    conn.close()

    logging.info(f"Data successfully written to {config.RAW_TABLE} table.")
