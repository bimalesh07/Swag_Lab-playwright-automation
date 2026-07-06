import pytest
from playwright.sync_api import Page, expect

class Login_Page:
    def __init__(self, page: Page, logger):
        self.page = page
        self.logger = logger
        
        # Locators
        self.username_textbox = "#user-name"
        self.password_textbox = "#password"
        self.login_button = "#login-button"
        self.header_title = "span.title" 
        self.invalid_error_message = "[data-test='error']"

    def Login_to_SourceLab(self, username, password):
        self.logger.info("************** START LOGIN ***********")
        self.page.locator(self.username_textbox).fill(username)
        self.page.locator(self.password_textbox).fill(password)
        self.page.locator(self.login_button).click()
        self.logger.info("************** LOGIN PROCESS COMPLETED ***********")

    def Verify_Login_display(self):
        self.logger.info("*********** Verifying Login Display Element ***********")
        return self.page.locator(self.header_title)
    
    def Error_login_page_message(self):
        self.logger.info("**********invalid Login **********************")
        return self.page.locator(self.invalid_error_message)