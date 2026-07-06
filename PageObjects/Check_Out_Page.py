from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page, logger):
        self.page = page
        self.logger = logger

        # Locators
        self.check_out_path = "#checkout"
        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.Postal_code = "#postal-code"
        self.continue_btn = "#continue"
        self.finish_btn = "#finish"          
        self.sucess_header = ".complete-header"

    def checkout_btn(self):
        self.logger.info("********Click the check out btn **********")
        self.page.locator(self.check_out_path).click()

    def fill_checkout_details(self, fname, lname, pcode):
        self.logger.info("*******Fill all the Details **************")
        self.page.locator(self.first_name).fill(fname)
        self.page.locator(self.last_name).fill(lname)
        self.page.locator(self.Postal_code).fill(pcode)
        self.page.locator(self.continue_btn).click() # Isse step-one complete ho gaya
    
    def click_finish_btn(self):               
        self.logger.info("************* Clicking Final Finish Button ***********")
        self.page.locator(self.finish_btn).click() 
        self.page.wait_for_timeout(1000)

    def get_sucessmesage(self):
        return self.page.locator(self.sucess_header)