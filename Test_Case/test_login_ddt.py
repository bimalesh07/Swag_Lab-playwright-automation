import pytest
from playwright.sync_api import expect
from PageObjects.Login_Page import Login_Page
from Uitilites.ReadJson import ReadJson

class TestLogin:
    @pytest.mark.parametrize("user_credentials", ReadJson.get_login_data())
    def test_swaglabs_login_ddt(self, fresh_url, user_credentials):
        """
        Unified Data-Driven Test case replacing individual valid/invalid tests.
        Uses your exact Page Object assertion methods.
        """
        page, logger = fresh_url
        logger.info(f" Starting DDT Scenario: {user_credentials['scenario']}")
        
        lp = Login_Page(page, logger)
        
     
        lp.Login_to_SourceLab(user_credentials["username"], user_credentials["password"])
        
   
        if user_credentials["is_valid"]:
            logger.info("Valid user detected. Verifying dashboard display...")
            expect(lp.Verify_Login_display()).to_be_visible()
            logger.info(f"********* {user_credentials['scenario']} Successfully **********")
            
        else:
            logger.info(f"Invalid user/empty field detected")
            expect(lp.Error_login_page_message()).to_contain_text(user_credentials["expected_error"])
            logger.info(f"********* {user_credentials['scenario']} Verified Successfully **********")