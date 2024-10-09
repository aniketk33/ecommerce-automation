import logging
import os
from datetime import datetime

class Logger:
    @staticmethod
    def get_logger():
        # Create logs directory if it doesn't exist
        if not os.path.exists("./logs"):
            os.makedirs("./logs")
        
        # Set the log file name with timestamp
        log_file = os.path.join("./logs", f"automation_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
        
        # Create logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # File handler to save logs to a file
        file_handler = logging.FileHandler(log_file, mode="a")
        file_handler.setLevel(logging.DEBUG)

        # Console handler to print logs to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Log format
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger