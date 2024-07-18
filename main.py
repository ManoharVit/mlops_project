from mlops import logger
from mlops.config.configuration import configurationManager
from mlops.components.data_ingestion import DataIngestion
from mlops.pipeline.stage_01_data_ingestion import DataIngestionTrainningPipeline

STAGE_NAME = "DATA INGESTION"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainningPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)