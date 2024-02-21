import pytest
import data
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
import time


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
    def test_is_answer_correct(self, driver, question_number, expected_result):
        mainPage = MainPage(driver)
        result = mainPage.scroll_down_then_click_on_question_and_get_answer_text(
            MainPageLocators.QUESTION_LOCATOR, MainPageLocators.ANSWER_LOCATOR, question_number)
        assert expected_result == result
