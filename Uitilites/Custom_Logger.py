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
        
    # 2. Har run ke liye ek unique log file ka naam (Optional, ya fir static automation.log rakh sakte ho)
    log_file = os.path.join(log_dir, "automation.log")
    
    # 3. Logger object create karo
    logger_obj = logging.getLogger("FrameworkLogger")
    logger_obj.setLevel(logging.INFO)
    
    # Avoid duplicate handlers if fixture runs multiple times
    if not logger_obj.handlers:
        # 4. Format set karo (Time | Log Level | Message)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        
        # 5. File Handler (Jo logs file me likhega)
        file_handler = logging.FileHandler(log_file, mode='a') # 'a' matlab append, purane logs ke niche naya judega
        file_handler.setFormatter(formatter)
        logger_obj.addHandler(file_handler)
        
        # 6. Console Handler (Jo terminal par bhi print karega)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger_obj.addHandler(console_handler)
        
    return logger_obj