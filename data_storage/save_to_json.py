# data_storage/save_to_json.py

import json  # Importing json to handle JSON operations
import os  # Importing os to interact with the operating system
from typing import Any  # Importing Any for type hinting

def save_data_to_json(data: Any, file_path: str, indent: int = 4):
    """
    Saves data to a JSON file.

    Args:
        data (Any): Data to be saved (e.g., dict, list).
        file_path (str): Path to the JSON file.
        indent (int): Indentation level for pretty-printing the JSON file.
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # Write data to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=indent)  # Serialize data to JSON