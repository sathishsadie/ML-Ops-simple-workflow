import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
## Tranforming the objects that the model expected format 
class DataTransformation:
    def __init__(self, data): ## Define the data
        self.data = data

    def transform(self): ## Tranform the categories or objects into the numbers using label Encoder
        cols = self.data.select_dtypes(include=['object','category'])
        lab_enc = [LabelEncoder() for i in range(len(cols))]
        for i, column in enumerate(cols):
            self.data[column] = lab_enc[i].fit_transform(self.data[column])
        return self.data,lab_enc
    
    def model_sav(self,model,dir): ## Save the model in the directory
        # os.makedirs(dir)
        with open(dir,'wb') as f:
            pickle.dump(model, f)

