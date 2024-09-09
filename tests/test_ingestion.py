import pytest
from src.ingestion import DataIngestion

def test_data_ingestion():
    # Initialize with test file path
    data_ingestion = DataIngestion('artifacts/train.csv')
    df = data_ingestion.read()

    # Check if data has been read
    assert not df.empty, "Data ingestion failed"
    assert 'Survived' in df.columns, "Target column missing in data"
