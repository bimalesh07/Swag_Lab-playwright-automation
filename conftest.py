from playwright.sync_api import sync_playwright
import os
from datetime import datetime
from Uitilites.Read_Env import ReadEnv
import pytest


@pytest.fixture(scope="class")
def page_setup():
    headless = False
    base_url = ReadEnv.get_base_url()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(base_url=base_url)
        page = context.new_page()
        

    

