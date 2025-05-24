import os
import urllib.request as request
from src.datascience.utils import logger
import zipfile
from src.datascience.entity.config_entity import (DataingestionConfig)
## Component Data Ingestion
class DataIngestion:
    def __init__(self,config:DataingestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} Downloaded with the following info: \n {headers}")
        else:
            logger.info(f"file already exists.")
            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        print(self.config.local_data_file)
        with zipfile.ZipFile(self.config.local_data_file,'r') as file:
            file.extractall(unzip_path)