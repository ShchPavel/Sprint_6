from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для main страницы. """

    # Локаторы для вопросов и ответов из блока 'Вопросы о важном'.
    QUESTION_LOCATOR = By.XPATH, '//div[@class=\'accordion__item\'][{}]'
    ANSWER_LOCATOR = By.XPATH, '//div[@class=\'accordion__item\'][{}]/div[@class=\'accordion__panel\']/p'

    # Локаторы для кнопок 'Заказать'.
    ORDER_BUTTON_IN_HEADER = By.CSS_SELECTOR, '.Header_Nav__AGCXC>.Button_Button__ra12g'
    ORDER_BUTTON_IN_BODY = By.CSS_SELECTOR, '.Home_FinishButton__1_cWm>.Button_Button__ra12g'

    # Локатор-индикатор нахождения на главной странице
    MAIN_PAGE_INDICATOR = By.CSS_SELECTOR, '.Home_Header__iJKdX'
