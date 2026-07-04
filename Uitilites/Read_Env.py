import os
from pathlib import Path
from dotenv import load_dotenv

current_folder = Path(__file__).resolve().parent
root_folder = current_folder.parent
env_file_path = root_folder / '.env'
load_dotenv(dotenv_path=env_file_path)

class ReadEnv:
    @staticmethod
    def get_base_url():
        return os.getenv("base_url")
    
    @staticmethod
    def get_username():
        return os.getenv("login_user")
    
    @staticmethod
    def get_password():
        return os.getenv("password")