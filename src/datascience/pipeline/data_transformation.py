from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience.utils.common import logger
from pathlib import Path

STAGE_NAME = 'Data Transformation'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_transformation(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'),'r') as file:
                status = file.read().split(' ')[-1] 
            print(status)
            if status == 'True':
                logger.info(f"Status is True and trying to split the training data and the test data")
                config = ConfigurationManager()
                data_transformation_config = config.get_transformation_config()
                data_tranformation = DataTransformation(data_transformation_config)
                data_tranformation.transform_data()
            else:
                raise Exception("The data Schema is not Valid")
        except Exception as err:
            raise err
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Started<<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_transformation()
        logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Completed<<<<<<<<<<<")
    except Exception as err:
        raise err