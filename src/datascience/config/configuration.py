from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import (DataingestionConfig)

class ConfigurationManager:
    def __init__(self,
                 config_file=CONFIG_FILE_PATH,
                 params_file=PARAMS_FILE_PATH,
                 schema_file=SCHEMA_FILE_PATH
                 ):
        self.config = read_yaml(config_file)
        self.params = read_yaml(params_file)
        self.schema = read_yaml(schema_file)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion(self)->DataingestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_confg = DataingestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_confg