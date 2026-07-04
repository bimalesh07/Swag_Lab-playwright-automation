import pytest
from playwright.sync_api import Browser # Built-in Type import kiya
from Uitilites.Read_Env import ReadEnv
from Uitilites.Custom_Logger import CustomLogger

logger = CustomLogger.get_logger()

@pytest.fixture(scope="class")
def class_page_setup(browser: Browser): 

    logger.info("[CLASS FIXTURE] Starting Browser Session")
    base_url = ReadEnv.get_base_url()

    context = browser.new_context(base_url=base_url)
    page = context.new_page()
    page.goto("/")
    
    yield page, logger

    logger.info("[CLASS FIXTURE] Tearing Down Browser Session")
    page.close()
    context.close()



"""Fresh url """
@pytest.fixture(scope="function")
def fresh_url(class_page_setup):
    page, logger = class_page_setup
    logger.info("[FUNCTION FIXTURE] Resetting Browser State & Cookies")
    
    page.context.clear_cookies()
    logger.info(" Cookies cleared successfully!")

    page.goto("/") 
    logger.info(" Navigated back to Fresh Base URL.")
    yield page, logger