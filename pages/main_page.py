from pages.base_page import BasePage


class MainPage(BasePage):

    url = 'https://qa-scooter.praktikum-services.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(self.url)

    def scroll_down_then_click_on_question_and_get_answer_text(self, question_locator, answer_locator, num):
        q_method, q_locator = question_locator
        test_question_locator = q_method, q_locator.format(num)
        a_method, a_locator = answer_locator
        test_answer_locator = a_method, a_locator.format(num)
        self.scroll_and_click_element(test_question_locator)
        return self.get_element_text(test_answer_locator)


