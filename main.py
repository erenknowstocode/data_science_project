from src.datascience.utils import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer import ModelTrainingPipeline
from src.datascience.pipeline.model_evaluation import ModelEvaluationPipeline

logger.info("Initating ML Pipeline")
STAGE_NAME_1 = 'Data Ingestion'
STAGE_NAME_2 = 'Data Validation'
STAGE_NAME_3 = 'Data Transformation'
STAGE_NAME_4 = 'Model Pipeline'
STAGE_NAME_5 = 'Model Evaluation'

try:
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME_1} Started<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME_1} Completed<<<<<<<<<<<")
except Exception as err:
    logger.exception(err)
    raise err

logger.info("=====================================================")

try:
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME_2} Started<<<<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.validate_data()
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME_2} Completed<<<<<<<<<<<")
except Exception as err:
    logger.exception(err)
    raise err

logger.info("=====================================================")

try:
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME_3} Started<<<<<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_transformation()
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME_3} Completed<<<<<<<<<<<")
except Exception as err:
    raise err 

logger.info("=====================================================")

try:
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME_4} Started<<<<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.initiate_training()
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME_4} Completed<<<<<<<<<<<")
except Exception as err:
    raise err

logger.info("=====================================================")

try:
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME_5} Started<<<<<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.initiate_evaluation()
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME_5} Completed<<<<<<<<<<<")
except Exception as err:
    raise err