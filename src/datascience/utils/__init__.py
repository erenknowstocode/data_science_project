import os
import logging
import sys

logging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s]"
logging_dir = 'logs'
logging_path = os.path.join(logging_dir,"logging.log")
os.makedirs(logging_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(logging_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("datasciencelogger")
