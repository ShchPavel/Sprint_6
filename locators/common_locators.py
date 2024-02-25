from selenium.webdriver.common.by import By


class CommonLocators:
    """ Локаторы для хедеров, общих для всех страница, и вспомогательные для проверки редиректа """

    # Локатор для кнопки  соглашения на использования куков, он возникает на любой странице сайта
    CONFIRM_COOKIES = By.ID, 'rcc-confirm-button'

    # Локаторы для кнопок в хедере на странице
    PAGE_HEADER_SAMOKAT_LOGO = By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR'
    PAGE_HEADER_YANDEX_LOGO = By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI'
    PAGE_HEADER_ORDER_BUTTON = By.CSS_SELECTOR, '.Header_Nav__AGCXC>.Button_Button__ra12g'

    # Локатор с главной страницы https://dzen.ru/?yredirect=true, используется как индикатор что страница загружена
    YANDEX_PAGE_IS_OPENED_INDICATOR = By.XPATH, '//button[text()=\'Найти\']'
