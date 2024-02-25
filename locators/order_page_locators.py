from selenium.webdriver.common.by import By


class OrderPageLocators:
    """ Локаторы для страницы /order. """

    # Локаторы для первого блока 'Для кого самокат'
    INPUT_NAME = By.XPATH, '//input[contains(@placeholder,\'Имя\')]'
    INPUT_SURNAME = By.XPATH, '//input[contains(@placeholder,\'Фамилия\')]'
    INPUT_ADDRESS = By.XPATH, '//input[contains(@placeholder,\'Адрес\')]'
    INPUT_METRO_STATION = By.XPATH, '//input[contains(@placeholder,\'Станция метро\')]'
    BUTTON_CHOOSING_SOKOLNIKI_STATION = By.XPATH, '//div[contains(text(), \'Сокольники\')]//parent::button'
    INPUT_PHONE = By.XPATH, '//input[contains(@placeholder,\'Телефон\')]'
    NEXT_BUTTON = By.CSS_SELECTOR, '.Order_NextButton__1_rCA>.Button_Button__ra12g'
    
    # Локаторы для второго блока 'Про Аренду'
    INPUT_DELIVERY_DATE = By.XPATH, '//input[contains(@placeholder,\'Когда\')]'
    BUTTON_DELIVERY_DATE_IN_CALENDAR = By.XPATH, '//div[text()=\'10\']'
    INPUT_RENT_TIME_PERIOD = By.XPATH, '//div[contains(text(),\'Срок аренды\')]'
    BUTTON_RENT_TIME_IN_LIST = By.XPATH, '//div[contains(text(),\'трое суток\')]'
    CHECKBOX_CHOOSE_BLACK_COLOR = By.XPATH, '//label[@for=\'black\']'
    CHECKBOX_CHOOSE_GREY_COLOR_CHECKBOX = By.XPATH, '//label[@for=\'grey\']'
    INPUT_COMMENT = By.XPATH, '//input[contains(@placeholder,\'Комментарий\')]'
    BUTTON_TO_MAKE_ORDER = By.XPATH, '//div[@class=\'Order_Buttons__1xGrp\']/button[text()=\'Заказать\']'
    CONFIRM_YES_BUTTON = By.XPATH, '//div[@class=\'Order_Buttons__1xGrp\']/button[text()=\'Да\']'
    CONFIRMATION_RESULT_TEXT = By.XPATH, '//div[@class=\'Order_ModalHeader__3FDaJ\']'

