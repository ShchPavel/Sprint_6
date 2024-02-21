from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import time
from helpers import DataGenerator


class OrderPage(BasePage):

    def fill_owner_info_form_and_confirm(self):
        self.set_element_input(OrderPageLocators.INPUT_NAME, DataGenerator().get_random_name())
        self.set_element_input(OrderPageLocators.INPUT_SURNAME, DataGenerator().get_random_surname())
        self.set_element_input(OrderPageLocators.INPUT_ADDRESS, DataGenerator().get_random_address())
        self.click_on_element(OrderPageLocators.INPUT_METRO_STATION)
        self.click_on_element(OrderPageLocators.BUTTON_CHOOSING_SOKOLNIKI_STATION)
        self.set_element_input(OrderPageLocators.INPUT_PHONE, DataGenerator().get_random_phone())
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    def fill_about_rent_form_and_confirm(self):
        self.click_on_element(OrderPageLocators.INPUT_DELIVERY_DATE)
        self.click_on_element(OrderPageLocators.BUTTON_DELIVERY_DATE_IN_CALENDAR)
        self.click_on_element(OrderPageLocators.INPUT_RENT_TIME_PERIOD)
        self.click_on_element(OrderPageLocators.BUTTON_RENT_TIME_IN_LIST)
        self.click_on_element(OrderPageLocators.CHECKBOX_CHOOSE_BLACK_COLOR)
        self.set_element_input(OrderPageLocators.INPUT_COMMENT, DataGenerator().get_random_comment())
        self.click_on_element(OrderPageLocators.BUTTON_TO_MAKE_ORDER)
        self.click_on_element(OrderPageLocators.CONFIRM_YES_BUTTON)
