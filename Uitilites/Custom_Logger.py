import logging
import os

class CustomLogger:
    @staticmethod
    def get_logger():
        # Logs folder banana agar nahi hai toh
        if not os.path.exists("Logs"):
            os.makedirs("Logs")

        logger = logging.getLogger("swagLab_Log")
        
        #logger
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(message)s", datefmt="%H:%M:%S")

            #print in console
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            # for save 
            file_handler = logging.FileHandler("logs/automation.log", mode="a")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger