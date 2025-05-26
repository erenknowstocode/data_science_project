import os
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_absolute_error, r2_score
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.utils.common import save_json
from pathlib import Path
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn 

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config
    
    def evaluation_metrics(self,actual,pred):
        rmse = np.sqrt(mean_absolute_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        
        return rmse, mae, r2
    
    def log_in_to_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[self.config.target_column]
        
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)
            
            (rmse, mae, r2) = self.evaluation_metrics(test_y,predicted_qualities)
            
            scores = {"rmse":rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metrics_file_name),data=scores)
            
            mlflow.log_params(self.config.all_params)
            
            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2",r2)
            
            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model,"model",registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model,"model")