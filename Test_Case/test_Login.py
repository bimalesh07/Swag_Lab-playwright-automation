import pytest
from Uitilites.Read_Env import ReadEnv
from PageObjects.Login_Page import LoginPage
from playwright.sync_api import expect

class TestLogin:
    pwd = ReadEnv.get_password()
    usr = ReadEnv.get_username()

    # Bracket me sirf 'class_page_setup' hona chahiye, 'page:Page' nahi!
    def test_loin(self, class_page_setup):
        page, logger = class_page_setup
        logger.info("********* Start Login Project ************")
        
        lp = LoginPage(page, logger)
        lp.Login_to_SourceLab(self.usr, self.pwd)  # Sahi order: usr pehle, pwd baad me

        expect(lp.Verify_Login_display()).to_be_visible()
        logger.info("********* Login Successfully **********")