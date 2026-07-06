import pytest
from Uitilites.Read_Env import ReadEnv
# 🌟 FIX: Purane LoginPage ko badal kar humne naya correct name Login_Page import kiya
from PageObjects.Login_Page import Login_Page 
from playwright.sync_api import expect

class TestLogin:
    pwd = ReadEnv.get_password()
    usr = ReadEnv.get_username()

    def test_login(self, class_page_setup):
        page, logger = class_page_setup
        logger.info("********* Start Login Project ************")
        
        lp = Login_Page(page, logger)
        lp.Login_to_SourceLab(self.usr, self.pwd)  

        expect(lp.Verify_Login_display()).to_be_visible()
        
        logger.info("********* Login Successfully **********")