import pandas as pd
from src.transformation import DataTransformation
from src.trianing import DataTraining
import os

## Data Ingestion phase read the data and send for the furthur process.
class DataIngestion:
    def __init__(self,dir):
        self.dir = dir
    def read(self):
        return pd.read_csv(os.path.join(os.path.dirname(__file__),self.dir))

if __name__ == '__main__':
    data_ingestion = DataIngestion('artifacts/train.csv')
    df = data_ingestion.read()
    
    ## Data Transformation phase performs necessary transformations on the data.
    data_transformation = DataTransformation(df)
    df_transformed,label_encoder = data_transformation.transform()
    data_transformation.model_sav(label_encoder,r'artifacts/tranformer.pkl')
    ## Data Training phase trains the model with the transformed data.
    data_training = DataTraining(df_transformed)
    x_tr,y_tr,x_te,y_te = data_training.split_data()
    model = data_training.train_model(x_tr,x_te,y_tr,y_te)
    
    ## Save the trained model for future use.
    data_transformation.model_sav(model,r'artifacts/model.pkl')