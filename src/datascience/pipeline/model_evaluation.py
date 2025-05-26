from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience.utils import logger
import os

os.environ['MLFLOW_TRACKING_URI'] ="https://dagshub.com/erenknowstocode/data_science_project.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME']="erenknowstocode"
os.environ['MLFLOW_TRACKING_PASSWORD']="02662f30438c4c9f1058932f8ddb8a8fd588daaf"

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.log_in_to_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Started<<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_evaluation()
        logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Completed<<<<<<<<<<<")
    except Exception as err:
        raise err