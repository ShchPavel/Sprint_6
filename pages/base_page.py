from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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

    def open_page(self, url):
        self.driver.get(url)

    def switch_to_browser_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])

    def get_current_url(self):
        return self.driver.current_url
