import logging
import sys

#Defining the format: Time - Name - Level - Message
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout) # Sends logs to my Docker terminal
        ]
    )
    return logging.getLogger("fastapi_app")

logger = setup_logging()