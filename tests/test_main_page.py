import pytest
import data
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
import allure


class TestMainPage:
    @pytest.mark.parametrize(
        "question_number, expected_result",
        [
            (1, data.Answers.answer_1),
            (2, data.Answers.answer_2),
            (3, data.Answers.answer_3),
            (4, data.Answers.answer_4),
            (5, data.Answers.answer_5),
            (6, data.Answers.answer_6),
            (7, data.Answers.answer_7),
            (8, data.Answers.answer_8)
        ]
    )
    @allure.title('Проверка корректного ответа при клике на вопрос №{question_number} в блоке "Вопросы о важном"')
    @allure.description('Кликаем на вопрос разделе "Вопросы о важном" и проверяем что ответ соответствует expected_result')
    def test_is_answer_for_question_correct(self, driver, question_number, expected_result):
        mainPage = MainPage(driver)
        mainPage.open_main_page_and_confirm_cookies()

        result = mainPage.scroll_down_then_click_on_question_and_get_answer_text(
            MainPageLocators.QUESTION_LOCATOR, MainPageLocators.ANSWER_LOCATOR, question_number)
        with allure.step('Проверяем, что ответ соответствует ожидаемому'):
            assert expected_result == result

    @allure.description('Кликаем на логотип Самокат в хедере страницы и проверяем успешность редиректа на '
                        'https://qa-scooter.praktikum-services.ru/')
    @allure.title('Проверка редиректа по нажатию на лого Самокат')
    def test_samokat_logo_redirect_to_main_page(self, driver):
        mainPage = MainPage(driver)
        mainPage.open_main_page_and_confirm_cookies()

        mainPage.click_samokat_logo_in_headers()
        with allure.step('Проверяем что произошел редирект на страницу "https://qa-scooter.praktikum-services.ru/"'):
            assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.description('Кликаем на логотип Яндекс в хедере страницы и проверяем успешность редиректа на https://dzen.ru/')
    @allure.title('Проверка редиректа при клике на лого Яндекс')
    def test_yandex_logo_redirect_to_dzen(self, driver):
        mainPage = MainPage(driver)
        mainPage.open_main_page_and_confirm_cookies()

        yandex_page_url = mainPage.click_yandex_logo_in_headers_and_check_redirect()
        with allure.step('Проверка редирект на страницу https://dzen.ru/ при нажатии на лого Яндекс'):
            assert 'https://dzen.ru/' in yandex_page_url
