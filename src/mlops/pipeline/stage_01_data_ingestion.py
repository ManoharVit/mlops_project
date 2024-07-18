from mlops import logger
from mlops.config.configuration import configurationManager
from mlops.components.data_ingestion import DataIngestion

STAGE_NAME = "DATA INGESTION"

class DataIngestionTrainningPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = configurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_files()
    

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainningPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)

