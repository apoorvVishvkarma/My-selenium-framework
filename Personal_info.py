from selenium.webdriver.common.by import By


class Personal:
    firstname = (By.ID,"first-name")
    lastname = (By.ID,"last-name")
    Zip = (By.ID,"postal-code")
    continyou = (By.ID,"continue")

    def __init__(self,driver):
        self.driver = driver

    def fname(self,firstname):
        self.driver.find_element(*self.firstname).send_keys(firstname)

    def sname(self,secondname):
        self.driver.find_element(*self.lastname).send_keys(secondname)

    def postal(self,zip):
        self.driver.find_element(*self.Zip).send_keys(zip)

    def done(self):
        self.driver.find_element(*self.continyou).click()





