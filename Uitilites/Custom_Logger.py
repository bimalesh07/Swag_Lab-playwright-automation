import os
import logging
from datetime import datetime
import pytest

@pytest.fixture(scope="session")
def logger():
    #create a logs folders if not exits in 
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    # uniue name
    log_file = os.path.join(log_dir, "automation.log")
    
    # Logger object create
    logger_obj = logging.getLogger("FrameworkLogger")
    logger_obj.setLevel(logging.INFO)
    
    # Avoid duplicate handlers if fixture runs multiple times
    if not logger_obj.handlers:
        # Format (Time | Log Level | Message)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        
        #File Handler (write in logs file )
        file_handler = logging.FileHandler(log_file, mode='a') # 'a' append
        file_handler.setFormatter(formatter)
        logger_obj.addHandler(file_handler)
        
        #print in terminal
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger_obj.addHandler(console_handler)
        
    return logger_obj