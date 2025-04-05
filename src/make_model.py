import os
import sys
import sqlite3
import pickle
import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
from src import config

def load_data():
    """Loads data from the SQLite database."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    query = f"SELECT col1, col2, colN FROM {config.PROCESSED_TABLE}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def train_model(grid_search=False):
    #Trains a the selected model with and saves evaluation metrics
    df = load_data()

    # Save original indices before vectorization
    df_indices = df.index

    # Feature extraction

    # Optional Save Model Vectorizer (pickle object)

    # Train-test split (preserve indices)
    
    # Save Model (pickle object)

    # Create a DataFrame for the test set with predictions to check against

    # Compute metrics
    metrics = {
        'metric1': metric1function(y_test, y_pred),
        'metric2': metric2function(y_test, y_pred),
        'metricN': metricNfunction(y_test, y_pred)
        }

    # Connect to the database to save test DataFrame and metrics
    conn = sqlite3.connect(config.DATABASE_PATH)

    # Saving predictions
    test_df.to_sql(config.PREDICTIONS_TABLE, conn, if_exists='replace', index=False)
    
    # Saving evaluation metrics
    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_sql(config.EVALUATION_TABLE, conn, if_exists='replace', index=False)

    # Commit and close the connection
    conn.commit()
    conn.close()