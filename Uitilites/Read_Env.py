import os
import pytest
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

current_folder = Path(__file__).resolve().parent
root_folder = current_folder.parent
env_file_path = root_folder / '.env'
load_dotenv(dotenv_path=env_file_path)



class ReadEnv:
    @staticmethod
    def get_base_url():
        return os.getenv("base_url")