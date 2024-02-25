import allure
from pages.main_page import MainPage


class TestRedirects:
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

        mainPage.click_yandex_logo_in_headers()
        yandex_page = mainPage.go_to_next_browser_tab_and_return_current_url()
        with allure.step('Проверяем что текущий url содержит https://dzen.ru/'):
            assert 'https://dzen.ru/' in yandex_page
