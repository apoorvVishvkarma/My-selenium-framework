




import pytest
from login import LoginPage
from Add_to_cart import ProductPage

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
    # step2.open_first_item()  # optional: open product before add-to-cart

    assert "cart" not in browser.current_url  # cart page abhi open nahi hua, sirf item add hua hai
