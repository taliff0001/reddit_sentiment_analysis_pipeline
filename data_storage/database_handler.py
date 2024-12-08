# data_storage/database_handler.py

import pandas as pd  # Importing pandas for data manipulation
from sqlalchemy import create_engine  # Importing create_engine to establish database connections
import yaml  # Importing yaml to handle YAML configuration files

def load_db_config(config_path: str) -> dict:
    """
    Loads database configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        dict: Database configuration parameters.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)  # Safely load the YAML configuration
    return config

def create_db_engine(config: dict):
    """
    Creates a SQLAlchemy engine using database configuration.

    Args:
        config (dict): Database configuration parameters.

    Returns:
        sqlalchemy.engine.base.Engine: SQLAlchemy engine object.
    """
    # Construct the database URL
    db_url = f"{config['dialect']}+{config['driver']}://" \
             f"{config['username']}:{config['password']}@" \
             f"{config['host']}:{config['port']}/{config['database']}"
    engine = create_engine(db_url)  # Create the SQLAlchemy engine
    return engine

def save_dataframe_to_db(df: pd.DataFrame, table_name: str, engine, if_exists: str = 'append'):
    """
    Saves a DataFrame to a database table.

    Args:
        df (pd.DataFrame): DataFrame to be saved.
        table_name (str): Name of the target database table.
        engine (sqlalchemy.engine.base.Engine): SQLAlchemy engine object.
        if_exists (str): Behavior when the table already exists. Options: 'fail', 'replace', 'append'.
    """
    df.to_sql(name=table_name, con=engine, if_exists=if_exists, index=False)  # Save DataFrame to the database