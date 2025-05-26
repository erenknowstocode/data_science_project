from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation
from src.datascience.utils.common import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def validate_data(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Started<<<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.validate_data()
        logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Completed<<<<<<<<<<<")
    except Exception as err:
        logger.exception(err)
        raise err