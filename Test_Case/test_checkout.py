import pytest
from playwright.sync_api import expect, Page
from Uitilites.Read_Env import ReadEnv
from PageObjects.Login_Page import Login_Page
from PageObjects.Dashbord_page import Dashbordpage
from PageObjects.Check_Out_Page import CheckoutPage

class TestCheckoutE2E:
    pwd = ReadEnv.get_password()
    usr = ReadEnv.get_username()

    def _step_login(self, page, logger):
        logger.info("--- Step: Logging into SauceLabs ---")
        lp = Login_Page(page, logger)
        lp.Login_to_SourceLab(self.usr, self.pwd)
        page.wait_for_timeout(1000)


    def _step_add_product_and_navigate_to_cart(self, page, logger):
        logger.info("--- Step: Adding product and moving to cart page ---")
        dp = Dashbordpage(page, logger)
        dp.add_to_cart()  
        page.wait_for_timeout(500)

        dp.cart_item()    
        page.wait_for_timeout(500)


    def _step_fill_checkout_and_verify(self, page, logger):
        logger.info("--- Step: Clicking Checkout and filling user details ---")
        chp = CheckoutPage(page, logger)
        
        chp.checkout_btn()  
        page.wait_for_timeout(500)
        
        chp.fill_checkout_details("Amit", "Sharma", "110001") 
        page.wait_for_timeout(500)

        chp.click_finish_btn()  
        page.wait_for_timeout(500)
        
        # Validation
        expect(chp.get_sucessmesage()).to_have_text("Thank you for your order!")

    @pytest.mark.regression 
    def test_end_to_end_checkout_workflow(self, class_page_setup):
        page,logger = class_page_setup
        logger.info("========= STARTING FULL CHECKOUT MASTER TEST =========")

        self._step_login(page, logger)
        self._step_add_product_and_navigate_to_cart(page, logger)
        self._step_fill_checkout_and_verify(page, logger)
        
        logger.info("========= FULL CHECKOUT MASTER TEST PASSED =========")