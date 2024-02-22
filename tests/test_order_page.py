import pytest
from locators.order_page_locators import OrderPageLocators
from locators.common_locators import CommonLocators
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
import allure


class TestOrderPage:

    @pytest.mark.parametrize("order_button", [
                                 CommonLocators.PAGE_HEADER_ORDER_BUTTON, MainPageLocators.ORDER_BUTTON_IN_BODY
                                ]
                             )
    @allure.title('Проверка успешного сценария оформления заказа')
    @allure.description('Проверяем успешный сценарий оформления заказа переходя на страницу с использованием локатора '
                        'order_button')
    def test_make_order_successful(self, driver, order_button):
        order_page = OrderPage(driver)
        order_page.open_main_page_and_confirm_cookies()

        order_page.scroll_and_click_element(order_button)
        order_page.fill_owner_info_form_and_confirm()
        order_page.fill_about_rent_form_and_confirm()
        with allure.step('Проверяем что в форме присутствует запись "Заказ оформлен", подтверждающая успешное оформление заказа'):
            assert 'Заказ оформлен' in order_page.get_element_text(OrderPageLocators.CONFIRMATION_RESULT_TEXT)
