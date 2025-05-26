import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.datascience.utils.common import logger
from src.datascience.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        
    def transform_data(self):
        data = pd.read_csv(self.config.data_path)
        
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
        
        logger.info('Splitting the data into train and test')
        logger.info(f"Training data shape: {train.shape}")
        logger.info(f"Testing data shape: {test.shape}")