from selenium.webdriver.common.by import By


class Payment:
    your_cart = (By.CLASS_NAME,"shopping_cart_link")
    Check_out = (By.ID,"checkout")

    def __init__(self,driver):
        self.driver = driver


    def cart(self):
        self.driver.find_element(*self.your_cart).click()

    def check(self):
        self.driver.find_element(*self.Check_out).click()