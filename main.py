from mlops import logger
from mlops.config.configuration import configurationManager
from mlops.components.data_ingestion import DataIngestion
from mlops.pipeline.stage_01_data_ingestion import DataIngestionTrainningPipeline
from mlops.pipeline.stage_02_data_validation import DataValidationTrainningPipeline

STAGE_NAME = "DATA INGESTION"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainningPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "DATA VALIDATION"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationTrainningPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)