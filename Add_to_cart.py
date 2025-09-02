from selenium.webdriver.common.by import By

class ProductPage:
    # Locators
    item = (By.CLASS_NAME, "inventory_item_name")  # first product
    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver

    def open_first_item(self):
        self.driver.find_element(*self.item).click()

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()