from locators.common_locators import CommonLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    """ Класс, описывающий методы для страницы main. """

    @allure.step('Скроллим страницу вниз, кликаем на вопрос')
    def scroll_down_then_click_on_question_and_get_answer_text(self, question_locator, answer_locator, num):
        q_method, q_locator = question_locator
        test_question_locator = q_method, q_locator.format(num)
        a_method, a_locator = answer_locator
        test_answer_locator = a_method, a_locator.format(num)
        self.scroll_and_click_element(test_question_locator)
        return self.get_element_text(test_answer_locator)

    @allure.step('Кликаем на логотип "Самокат" в хедере страницы')
    def click_samokat_logo_in_headers(self):
        self.click_on_element(CommonLocators.PAGE_HEADER_SAMOKAT_LOGO)
        self.wait_and_find_element(MainPageLocators.MAIN_PAGE_INDICATOR)

    @allure.step('Кликаем на логотип "Яндекс" в хедере страницы')
    def click_yandex_logo_in_headers_and_check_redirect(self):
        self.click_on_element(CommonLocators.PAGE_HEADER_YANDEX_LOGO)
        self.driver.switch_to.window(self.driver.window_handles[1])
        if self.is_element_exist(CommonLocators.YANDEX_PAGE_IS_OPENED_INDICATOR) is True:
            return self.driver.current_url
