import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths for raw data (Excel files)
RAW_DATA_PATH = os.path.join(BASE_DIR, "../data/raw/")

# Path for manual preprocessing
LOADING_DATA_PATH = os.path.join(BASE_DIR, "../src/")

# SQLite Database Path
DATABASE_PATH = os.path.join(BASE_DIR, "../database/sqlite.db")

# Preprocessed Data Table Name
PROCESSED_TABLE = "lorem_ipsum"

# Raw Data Table Name
RAW_TABLE = "raw_table_name"

# Predictions Table Name
PREDICTIONS_TABLE = "predictions"

# Logging Configuration
LOGGING_LEVEL = "INFO"

# Saved models
MODELS_PATH = "../models/"