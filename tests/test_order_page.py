import pytest
from locators.common_locators import CommonLocators
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
import allure
from pages.main_page import MainPage


class TestOrderPage:

    @pytest.mark.parametrize(("order_button", "button_descriptioon"), [
        (CommonLocators.PAGE_HEADER_ORDER_BUTTON, "Кнопка заказа в хедере страницы"),
        (MainPageLocators.ORDER_BUTTON_IN_BODY, "Кнопка заказа в теле страницы")
                                ]
                             )
    @allure.title('Проверка успешного сценария оформления заказа')
    @allure.description('Проверяем успешный сценарий оформления заказа переходя на страницу с использованием локатора '
                        'order_button')
    def test_make_order_successful(self, driver, order_button, button_descriptioon):
        MainPage(driver).open_main_page_and_confirm_cookies()
        order_page = OrderPage(driver)

        with allure.step(f'Нажимаем на элемент "{button_descriptioon}"'):
            order_page.scroll_and_click_element(order_button)
        order_page.fill_owner_info_form_and_confirm()
        order_page.fill_about_rent_form_and_confirm()
        with allure.step('Проверяем что в тексте присутствует запись "Заказ оформлен", подтверждающая успешное оформление заказа'):
            assert 'Заказ оформлен' in order_page.get_success_order_approve_text()
