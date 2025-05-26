from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import Modeltrainer
from src.datascience.utils import logger

STAGE_NAME = "Model Trainer"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = Modeltrainer(model_trainer_config)
        model_trainer.train()
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Started<<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_training()
        logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Completed<<<<<<<<<<<")
    except Exception as err:
        raise err