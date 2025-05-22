import os
import yaml
from src.datascience.utils import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exception import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty.")
    
    except Exception as err:
        raise err
    
@ensure_annotations
def create_directories(path_to_dir: list,verbose=True):
    for path in path_to_dir:
        os.makedirs(path, exist_ok=True)
        
        if verbose:
            logger.info(f"Created directory at: {path}")
            
@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as file:
        json.dump(data,file, indent=4)
    
    logger.info(f"Json file saved at: {path}")
    
@ensure_annotations
def load_json(path: Path):
    with open(path,"r") as file:
        content = json.load(file)
    
    logger.info(f"Json file loaded successfully from: {path}")
    return content
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path):
    data = joblib.load(path)
    logger.info(f"Json file loaded successfully from: {path}")
    
    return data