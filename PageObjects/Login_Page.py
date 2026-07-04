from playwright.sync_api import sync_playwright, expect, Page
from Uitilites.Custom_Logger import CustomLogger
from Uitilites.Read_Env import ReadEnv

class LoginPage:

    def __init__(self, page:Page, logger):
        self.page = page
        self.logger = logger

        #locaters
        self.input_username = "#user-name"
        self.input_password = "#password"
        self.login_btn = "#login-button"
        self.logo_visible = ".app_logo"

    def Login_to_SourceLab(self,userane, password):
        self.logger.info("**************START LOGN ***********")
        self.page.locator(self.input_username).fill(userane)
        self.page.locator(self.input_password).fill(password)

        btn_click = self.page.locator(self.login_btn)
        btn_click.click()
    
    def Verify_Login_display(self):
        return self.page.locator(self.logo_visible)



