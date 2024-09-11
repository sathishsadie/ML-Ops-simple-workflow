# tests/test_ingestion.py
import pytest
import pandas as pd
from src.ingestion import DataIngestion
import os
# print(os.path.dirname(__file__))
def test_data_ingestion():
    data_ingestion = DataIngestion(r'artifacts/train.csv')  # Use a sample data file path
    df = data_ingestion.read()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
test_data_ingestion()