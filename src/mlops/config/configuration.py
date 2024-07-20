from mlops.constants import * 
from mlops.utils.common import read_yaml,create_directories
from mlops.entity.config_entity import DataIngestionConfig, DataValidationconfig

class configurationManager:
    def __init__(
            self,
            config_file_path = CONFIG_FILE_PATH,
            params_file_path = PARAMS_FILE_PATH,
            schema_file_path = SCHEMA_FILE_PATH
    ):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            local_data_file=config.local_data_file,
            source_URL= config.source_URL,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationconfig:
            config = self.config.data_validation
            schema = self.schema.COLUMNS

            create_directories([config.root_dir])

            data_validation_config = DataValidationconfig(
                 root_dir = config.root_dir,
                 status_file = config.status_file,
                 unzip_dir = config.unzip_dir,
                 all_schema = schema
            )
            
            return data_validation_config



