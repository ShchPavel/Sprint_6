import pytest
import data
from pages.main_page import MainPage
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

        result = mainPage.scroll_down_then_click_on_question_and_get_answer_text(question_number)
        with allure.step('Проверяем, что ответ соответствует ожидаемому'):
            assert expected_result == result

