from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls
from locators.common_locators import CommonLocators
import allure


class BasePage:
    """ Класс, описывающий взаимодействия с элементами. """

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    def get_element_text(self, locator):
        element = self.wait_and_find_element(locator)
        return element.text

    def set_element_input(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)

    def scroll_and_click_element(self, locator):
        element = self.wait_and_find_element(locator)
        ActionChains(self.driver).move_to_element(element)
        element.click()

    def is_element_exist(self, locator):
        if self.wait_and_find_element(locator) is not None:
            return True

    @allure.step('Открываем страницу https://qa-scooter.praktikum-services.ru/ и принимаем использование cookies')
    def open_main_page_and_confirm_cookies(self):
        self.driver.get(Urls.main_url)
        self.click_on_element(CommonLocators.CONFIRM_COOKIES)
