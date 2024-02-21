from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
import time
from pages.order_page import OrderPage
from selenium.webdriver.common.action_chains import ActionChains


class TestOrderPage:

    def test_1(self, driver):
        MainPage(driver).click_on_element(MainPageLocators.ORDER_BUTTON_IN_HEADER)
        order_page = OrderPage(driver)
        order_page.fill_owner_info_form_and_confirm()
        order_page.fill_about_rent_form_and_confirm()
        assert 'Заказ оформлен' in order_page.get_element_text(OrderPageLocators.CONFIRMATION_RESULT_TEXT)

    def test_2(self, driver):
        MainPage(driver).scroll_and_click_element(MainPageLocators.ORDER_BUTTON_IN_BODY)
        order_page = OrderPage(driver)
        order_page.fill_owner_info_form_and_confirm()
        order_page.fill_about_rent_form_and_confirm()
        assert 'Заказ оформлен' in order_page.get_element_text(OrderPageLocators.CONFIRMATION_RESULT_TEXT)