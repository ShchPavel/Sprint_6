from selenium import webdriver
import pytest
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    #driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.set_window_size(1920, 1080)
    MainPage(driver).click_on_element(MainPageLocators.CONFIRM_COOKIES)
    yield driver
    driver.quit()

