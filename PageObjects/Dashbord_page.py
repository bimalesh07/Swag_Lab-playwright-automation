from playwright.sync_api import Page  # Sirf type hinting ke liye zaroori hai

class Dashbordpage:
    def __init__(self, page: Page, logger):
        self.page = page
        self.logger = logger

        # Locators for Dashboard Page
        self.filter_dropdown = ".product_sort_container"
        self.item_names = ".inventory_item_name"
        self.items_price = ".inventory_item_price"
        self.add_to_cart_path = "#add-to-cart-sauce-labs-backpack"
        
        # Locators for Cart Page Action
        self.Cart_link_path = ".shopping_cart_link"  
        self.checkout_btn_visible = "#checkout"
    
    def sort_products_by_value(self, option_value):
        self.logger.info(f"******* Checking Dropdown filters for value: {option_value} **********")
        self.page.locator(self.filter_dropdown).select_option(value=option_value)
        self.logger.info("********** Filters selection completed *************")

    def get_by_names(self):
        self.logger.info("*********** Fetching product names from UI ***********")
        return self.page.locator(self.item_names).all_text_contents()
    
    def get_by_price(self):
        self.logger.info("******** Fetching product prices from UI **********************")
        pricess_elements = self.page.locator(self.items_price).all_text_contents()
        return [float(price.replace("$", "")) for price in pricess_elements]


    def add_to_cart(self):
        self.logger.info("***** Add to cart **************")
        self.page.locator(self.add_to_cart_path).click()

  
    def cart_item(self):
        self.logger.info("********** Clicking the cart box item *********")
        self.page.locator(self.Cart_link_path).click()

    def get_checkout_button(self):
        self.logger.info("Fetching checkout button locator from Cart Page")
        return self.page.locator(self.checkout_btn_visible)
  