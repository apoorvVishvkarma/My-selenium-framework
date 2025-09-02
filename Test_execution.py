import time
import pytest

from login import LoginPage
from Add_to_cart import ProductPage
from checkout import Payment
from Personal_info import Personal


def test_submit(browser):
    step1 = LoginPage(browser)

    # Open site
    step1.open_page("https://www.saucedemo.com/")

    # Perform login
    step1.enter_username("standard_user")
    step1.enter_password("secret_sauce")
    step1.log_in()

    # Assertion - check if login successful
    assert "inventory" in browser.current_url


def test_pro(browser):
    step1 = LoginPage(browser)
    step2 = ProductPage(browser)

    # Open site
    step1.open_page("https://www.saucedemo.com/")

    # Perform login
    step1.enter_username("standard_user")
    step1.enter_password("secret_sauce")
    step1.log_in()

    # Perform product actions
    step2.add_to_cart()

    assert "cart" not in browser.current_url
    time.sleep(4)


def test_check(browser):
    step1 = LoginPage(browser)
    step2 = ProductPage(browser)
    step3 = Payment(browser)

    # Open site
    step1.open_page("https://www.saucedemo.com/")

    # Perform login
    step1.enter_username("standard_user")
    step1.enter_password("secret_sauce")
    step1.log_in()

    # Perform product actions
    step2.add_to_cart()

    # perform cart page actions
    step3.cart()
    step3.check()

    time.sleep(4)


def test_alldone(browser):
    step1 = LoginPage(browser)
    step2 = ProductPage(browser)
    step3 = Payment(browser)
    step4 = Personal(browser)

    # Open site
    step1.open_page("https://www.saucedemo.com/")

    # Perform login
    step1.enter_username("standard_user")
    step1.enter_password("secret_sauce")
    step1.log_in()

    # Perform product actions
    step2.add_to_cart()


    # Cart page
    step3.cart()
    step3.check()



    # Fill personal info
    step4.fname("Apoorv")
    step4.sname("Sharma")
    step4.postal("123456")
    step4.done()
