from mlops import logger
from mlops.config.configuration import configurationManager
from mlops.components.data_validation import DataValidation

STAGE_NAME = "DATA VALIDATION"

class DataValidationTrainningPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = configurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()
    

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataValidationTrainningPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)