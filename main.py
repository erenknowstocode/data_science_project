from src.datascience.utils import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline

logger.info("Initating ML Pipeline")
STAGE_NAME = 'Data Ingestion'

try:
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Started<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Completed<<<<<<<<<<<")
except Exception as err:
    logger.exception(err)
    raise err