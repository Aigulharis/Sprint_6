import pytest
import allure
from locators.main_page_locators import MainPageLocators
from helpers import generate_fill_personal_info
from pages.order_page import OrderPage


class TestOrderPageOrder:

    @allure.title('Проверка флоу позитивного сценария оформления заказа')
    @allure.description('Тест функциональности оформления заказа из двух точек входа')
    @pytest.mark.parametrize('button', [
        MainPageLocators.ORDER_BUTTON_MAIN,
        MainPageLocators.ORDER_BUTTON_MAIN_BELOW
    ])
    def test_order_all_fields_success(self, driver, button):
        # Генерируем личные данные один раз внутри теста
        personal_info = generate_fill_personal_info()
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_for_element(button)
        order_page.click_on_element(button)
        order_page.data_entry_first_form(personal_info)
        order_page.data_entry_second_form(personal_info)
        assert order_page.check_the_order_data_page_display()

class TestLogoRedirect:
    @allure.title('Проверка перехода на главную страницу при клике на лого "Самокат" в шапке')
    def test_logo_redirect_to_main_page_success(self, driver):
        order_page = OrderPage(driver)
        order_page.wait_for_element_logo_scooter()
        order_page.click_on_logo_scooter()
        order_page.wait_for_element_of_main_header()
        assert order_page.check_displaying_main_header()

    @allure.title('Проверка перехода на страницу "Дзен" при клике на лого "Яндекс"')
    def test_logo_redirect_to_dzen_success(self, driver):
        order_page = OrderPage(driver)
        order_page.wait_for_element_logo_yandex()
        order_page.click_on_logo_yandex()
        order_page.switch_to_next_tab()
        order_page.wait_and_get_url(expected_url="https://dzen.ru/?yredirect=true")
        assert order_page.check_transition_page_dzen()
