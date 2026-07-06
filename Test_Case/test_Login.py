import pytest
from Uitilites.Read_Env import ReadEnv
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
    
    """Invalid username and password"""
    def test_invlid_username_password(self, fresh_url):
        page, logger = fresh_url
        logger.info("*******invalid username*******")
        
        lp = Login_Page(page, logger)
        lp.Login_to_SourceLab("bimalesh", "yadav")

        expect(lp.Error_login_page_message()).to_contain_text(
            "Epic sadface: Username and password do not match any user in this service"
        )
        logger.info("********* Invalid Login Verified Successfully **********")
    
        
    """empty username """
    def test_empty_username(self, fresh_url):
        page, logger = fresh_url
        logger.info("*******invalid username*******")
        
        lp = Login_Page(page, logger)
        lp.Login_to_SourceLab("", "yadav")

        expect(lp.Error_login_page_message()).to_contain_text(
            "Epic sadface: Username is required"
        )
        logger.info("********* Invalid Login Verified Successfully **********")

        
    """empty password """
    def test_empty_password(self, fresh_url):
        page, logger = fresh_url
        logger.info("*******invalid username*******")
        
        lp = Login_Page(page, logger)
        lp.Login_to_SourceLab("bimalesh", "")

        expect(lp.Error_login_page_message()).to_contain_text(
            "Epic sadface: Password is required"
        )
        logger.info("********* Invalid Login Verified Successfully **********")