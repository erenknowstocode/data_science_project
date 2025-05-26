from src.datascience.utils import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation import DataTransformationTrainingPipeline
logger.info("Initating ML Pipeline")
STAGE_NAME_1 = 'Data Ingestion'
STAGE_NAME_2 = 'Data Validation'
STAGE_NAME_3 = 'Data Transformation'

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