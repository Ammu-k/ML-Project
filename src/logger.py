import logging
import os
from datetime import datetime

LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)   #cwd = current working directory
os.makedirs(logs_path, exist_ok=True)   #This will create the logs directory if it does not exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,   #This will log all the messages with level INFO and above (INFO, WARNING, ERROR, CRITICAL)
)