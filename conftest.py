from playwright.async_api import async_playwright
import os
from datetime import datetime
from Uitilites.Read_Env import ReadEnv
import pytest


@pytest.fixture(scope="class")
def page_setup():
    headless = False
    base_url = ReadEnv.get_base_url()
    browser = pa

    

