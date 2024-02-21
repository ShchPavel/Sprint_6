from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """ Абстрактный класс, описывающий взаимодействия с элементами. """

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
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
