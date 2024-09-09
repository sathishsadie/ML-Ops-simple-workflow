from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
### Training the model and evaluate and find the best model
class DataTraining:
    def __init__(self,data): ### Get the Data
        self.data = data

    def split_data(self, test_size=0.2): ## Split the categories into features and labels and split for testing and training
        self.X = self.data.drop('Survived', axis=1)
        self.y = self.data['Survived']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=test_size, random_state=42)
        return self.X_train, self.X_test, self.y_train, self.y_test
    
    def train_model(self,X,y,x_te,y_te): ## Train the model and evaluate its performances usign test data
        models = {
            'logisticRegression': LogisticRegression(),
            'randomforestClassifier': RandomForestClassifier(),
            'DecisionTree':DecisionTreeClassifier()
        }
        perfomances={}
        for name,model in models.items():
            model.fit(X, y)
            accuracy = self.test_model(model,x_te,y_te)
            perfomances[name] = accuracy
        
        name_best_model = max(perfomances, key=perfomances.get)
        return models[name_best_model]
    

    def test_model(self,model,x_te,y_te): ## For evaluating the performance of the model
        preds = model.predict(x_te)
        return accuracy_score(y_te,preds)