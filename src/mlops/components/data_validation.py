import os
from mlops import logger
import pandas as pd
from mlops.config.configuration import DataValidationconfig

class DataValidation:
    def __init__(self,config: DataValidationconfig):
        self.config = config
        
    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            data = pd.read_csv(self.config.unzip_dir)
            schema = self.config.all_schema

            for column in schema.keys():
                if column not in data.columns:
                    validation_status= False
                    self._write_status_file(False,f"Missing Column: {column}")
                    return validation_status
            
            for column,expected_dtype in schema.items():
                if column in data.columns:
                    actual_dtype = str(data[column].dtype)
                    if actual_dtype != expected_dtype:
                        validation_status = False
                        self._write_status_file(False,f"Column {column} is of type {actual_dtype} but expecting {expected_dtype}")
                        return validation_status
        except Exception as e:
            self._write_status_file(False,f"Exception occured: {str(e)}")
            raise e
        
    def _write_status_file(self,status: bool,message: str):
        with open(self.config.status_file,'w') as f:
            f.write(f"Validation Status: {status}\n")
            f.write(message)