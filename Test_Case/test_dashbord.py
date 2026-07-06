import pytest
from playwright.sync_api import expect
from Uitilites.Read_Env import ReadEnv
from PageObjects.Login_Page import Login_Page
from PageObjects.Dashbord_page import Dashbordpage

class TestDashboard:
    # Class level configuration credentials
    pwd = ReadEnv.get_password()
    usr = ReadEnv.get_username()

    def _step_login(self, page, logger):
        logger.info("--- Step: Logging into the application ---")
        lp = Login_Page(page, logger)
        lp.Login_to_SourceLab(self.usr, self.pwd)
        page.wait_for_timeout(1000)

    def _step_verify_dropdown_filters(self, page, logger, dp):
        logger.info("--- Step: Verifying All Dropdown Filters ---")
        all_filters = ["az", "za", "lohi", "hilo"]
        
        for sort_value in all_filters:
            logger.info(f"Applying Filter Dynamically: {sort_value}")
            dp.sort_products_by_value(sort_value)
            page.wait_for_timeout(500) 
            
            if sort_value == "az":
                actual_names = dp.get_by_names()
                assert actual_names == sorted(actual_names), f"Validation Failed: {sort_value}"
                
            elif sort_value == "za":
                actual_names = dp.get_by_names()
                assert actual_names == sorted(actual_names, reverse=True), f"Validation Failed: {sort_value}"
                
            elif sort_value == "lohi":
                actual_prices = dp.get_by_price()
                assert actual_prices == sorted(actual_prices), f"Validation Failed: {sort_value}"
                
            elif sort_value == "hilo":
                actual_prices = dp.get_by_price()
                assert actual_prices == sorted(actual_prices, reverse=True), f"Validation Failed: {sort_value}"
                
            logger.info(f"Validation Passed for Filter: '{sort_value}' successfully!")

    def _step_add_to_cart(self, page, logger, dp):
        logger.info("--- Step: Adding product to cart ---")
        dp.add_to_cart() 
        page.wait_for_timeout(500)


    def _step_click_cart_and_verify_checkout(self, page, logger, dp):
        logger.info("--- Step: Clicking Cart Icon & Verifying Checkout Page ---")
        
        # 1. Page file ke function se click kiya
        dp.cart_item()
        page.wait_for_timeout(500) 
        
      
        expect(dp.get_checkout_button()).to_be_visible()
        logger.info("Success: Navigated to cart and checkout button is perfectly visible!")


    #pytest run this test fun
    def test_complete_dashboard_end_to_end_flow(self, class_page_setup):
        page, logger = class_page_setup
        logger.info("========= STARTING MAIN PROFESSIONAL E2E SUITE =========")
        
        self._step_login(page, logger)
        dp = Dashbordpage(page, logger)
        
        #self._step_verify_dropdown_filters(page, logger, dp)
        self._step_add_to_cart(page, logger, dp)
        self._step_click_cart_and_verify_checkout(page, logger, dp)
        
        logger.info("========= MAIN E2E SUITE PASSED COMPLETELY =========")