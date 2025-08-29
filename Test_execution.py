import pytest
from login import LoginPage

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



