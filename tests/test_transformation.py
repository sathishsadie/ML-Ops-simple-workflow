import pytest
from src.transformation import DataTransformation
import pandas as pd

@pytest.fixture
def sample_data():
    # Mock sample data to test transformation
    data = {'Sex': ['male', 'female'], 'Embarked': ['S', 'C'], 'Survived': [0, 1]}
    df = pd.DataFrame(data)
    return df

def test_data_transformation(sample_data):
    # Initialize transformation class
    data_transformation = DataTransformation(sample_data)
    df_transformed, label_encoder = data_transformation.transform()

    # Check if transformation has been applied correctly
    assert 'Sex' in df_transformed.columns, "Transformation failed"
    assert df_transformed['Sex'].dtype == 'int32', "Sex column was not transformed properly"
