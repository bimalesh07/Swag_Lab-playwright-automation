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


import pytest
import base64

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # These match  fixture names: 'fresh_url' and 'class_page_setup'
        fixture_names = ["fresh_url", "class_page_setup"]
        page_obj = None

        # Look for the active page object in the current running test
        for name in fixture_names:
            if name in item.funcargs:
                fixture_value = item.funcargs[name]
                
                # SwagLabs fixtures return a tuple (page, logger), 
                # we extract the page using index 0
                if isinstance(fixture_value, tuple):
                    page_obj = fixture_value[0]
                else:
                    page_obj = fixture_value
                break

        # If we successfully found the browser page, capture the screenshot
        if page_obj:
            try:
                #Take the screenshot in memory (no file saved pc)
                screenshot_bytes = page_obj.screenshot(type="png")
                
                #Convert the image bytes into a clean Base64 text string
                encoded_screenshot = base64.b64encode(screenshot_bytes).decode("utf-8")
                
                #Create the HTML image element
                html_img = f'<div><img src="data:image/png;base64,{encoded_screenshot}" alt="screenshot" style="width:600px;height:auto;border:1px solid red;margin-top:10px;"/></div>'
                
                #Inject it into the pytest report data
                extra.append(pytest_html.extras.html(html_img))
                report.extra = extra
                
            except Exception as e:
                print(f"\n[REPORT ERROR] Could not capture browser screenshot: {e}")

#import check for pytest_html library
try:
    import pytest_html
except ImportError:
    pass