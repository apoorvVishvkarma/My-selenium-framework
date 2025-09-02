import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture
def browser():
    options = EdgeOptions()


    service = EdgeService()
    driver = webdriver.Edge(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
