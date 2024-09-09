import pytest # type: ignore
from src.trianing import DataTraining
import pandas as pd

@pytest.fixture
def sample_transformed_data():
    # Mock sample data for testing training
    data = {'Sex': [1, 0,1,0,1], 'Embarked': [0, 1,2,3,2], 'Survived': [0, 1,1,1,1]}
    df = pd.DataFrame(data)
    return df

def test_model_training(sample_transformed_data):
    # Initialize training class

    data_training = DataTraining(sample_transformed_data)
    x_tr, x_te, y_tr, y_te = data_training.split_data()

    # Check if split was successful
    assert len(x_tr) > 0 and len(x_te) > 0, "Data split failed"
    
    # Train model and check if it's trained
    model = data_training.train_model(x_tr, y_tr, x_te, y_te)
    assert model is not None, "Model training failed"
