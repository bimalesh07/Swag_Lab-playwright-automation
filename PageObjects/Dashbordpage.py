import pytest
from playwright.sync_api import Page, expect


class Dashbordpage:

    def __int__(self, page:Page, logger):
        self.page = page
        self.logger = logger

        fillter_dropwon = ""
    
    def fillters_dropdown(self,  option_value):
        self.logger.info("*******Checking Dropdown fillters **********")

        