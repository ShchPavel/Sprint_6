from data import Urls
from locators.common_locators import CommonLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    """ Класс, описывающий методы для страницы main. """

    @allure.step('Открываем страницу https://qa-scooter.praktikum-services.ru/ и принимаем использование cookies')
    def open_main_page_and_confirm_cookies(self):
        self.open_page(Urls.main_url)
        self.click_on_element(CommonLocators.CONFIRM_COOKIES)

    @allure.step('Скроллим страницу вниз, кликаем на вопрос и получаем текст ответа')
    def scroll_down_then_click_on_question_and_get_answer_text(self, question_number):
        q_method, q_locator = MainPageLocators.QUESTION_LOCATOR
        test_question_locator = q_method, q_locator.format(question_number)
        a_method, a_locator = MainPageLocators.ANSWER_LOCATOR
        test_answer_locator = a_method, a_locator.format(question_number)
        self.scroll_and_click_element(test_question_locator)
        return self.get_element_text(test_answer_locator)

    @allure.step('Кликаем на логотип "Самокат" в хедере страницы')
    def click_samokat_logo_in_headers(self):
        self.click_on_element(CommonLocators.PAGE_HEADER_SAMOKAT_LOGO)
        self.wait_and_find_element(MainPageLocators.MAIN_PAGE_INDICATOR)

    @allure.step('Кликаем на логотип "Яндекс" в хедере страницы')
    def click_yandex_logo_in_headers(self,):
        self.click_on_element(CommonLocators.PAGE_HEADER_YANDEX_LOGO)

    @allure.step('Переключаемся на новую вкладку при редиректе и получаем ее url')
    def go_to_next_browser_tab_and_return_current_url(self):
        self.switch_to_browser_tab(1)
        if self.is_element_exist(CommonLocators.YANDEX_PAGE_IS_OPENED_INDICATOR) is True:
            return self.get_current_url()
