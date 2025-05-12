import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from .base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def data_entry_first_form(self, personal_info):
        name, last_name, address, phone, metro, date, comment = personal_info
        self.wait_for_element(OrderPageLocators.INPUT_NAME)
        self.click_on_element(OrderPageLocators.INPUT_NAME)
        self.send_keys_to_input(OrderPageLocators.INPUT_NAME, name)
        self.click_on_element(OrderPageLocators.INPUT_LAST_NAME)
        self.send_keys_to_input(OrderPageLocators.INPUT_LAST_NAME, last_name)
        self.click_on_element(OrderPageLocators.INPUT_ADDRESS)
        self.send_keys_to_input(OrderPageLocators.INPUT_ADDRESS, address)
        self.click_on_element(OrderPageLocators.INPUT_METRO)
        self.send_keys_to_input(OrderPageLocators.INPUT_METRO, metro)
        self.click_on_element(OrderPageLocators.SELECT_ITEM_METRO)
        self.click_on_element(OrderPageLocators.INPUT_PHONE)
        self.send_keys_to_input(OrderPageLocators.INPUT_PHONE, phone)
        self.click_on_element(OrderPageLocators.FURTHER_BUTTON)

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def data_entry_second_form(self, personal_info):
        name, last_name, address, phone, metro, date, comment = personal_info
        self.wait_for_element(OrderPageLocators.TITLE_PAGE_ABOUT_RENT)
        self.click_on_element(OrderPageLocators.INPUT_WHEN_BRING)
        self.send_keys_to_input(OrderPageLocators.INPUT_WHEN_BRING, date)
        #self.click_on_element(OrderPageLocators.CALENDAR)
        #self.send_keys_to_input(OrderPageLocators.CALENDAR_ELEMENT, date)
        self.click_on_element(OrderPageLocators.CHECKBOX_COLOR_SCOOTER_BLACK)
        self.click_on_element(OrderPageLocators.INPUT_RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.DROPDOWN_LIST_RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.INPUT_COMMENT_COURIER)
        self.send_keys_to_input(OrderPageLocators.INPUT_COMMENT_COURIER, comment)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.wait_for_element(OrderPageLocators.ORDER_YES_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_YES_BUTTON)
        self.click_on_element(OrderPageLocators.WATCH_STATUS_BUTTON)

    @allure.step('Проверить отображение страницы данных о заказе')
    def check_the_order_data_page_display(self):
        return self.wait_for_element(OrderPageLocators.ORDER_INFORMATION_PAGE)

    @allure.step('Подождать загрузки части лого с надписью "Яндекс" в хэдере')
    def wait_for_element_logo_yandex(self):
        self.wait_for_element(OrderPageLocators.LOGO_YANDEX)

    @allure.step('Кликнуть по части лого с надписью "Яндекс" в хэдере')
    def click_on_logo_yandex(self):
        self.click_on_element(OrderPageLocators.LOGO_YANDEX)

    @allure.step('Подождать загрузки части лого с надписью "Самокат" в хэдере')
    def wait_for_element_logo_scooter(self):
        self.wait_for_element(OrderPageLocators.LOGO_SCOOTER)

    @allure.step('Кликнуть по части лого с надписью "Самокат" в хэдере')
    def click_on_logo_scooter(self):
        self.click_on_element(OrderPageLocators.LOGO_SCOOTER)

    @allure.step('Подождать загрузки отображения заголовка главной страницы')
    def wait_for_element_of_main_header(self):
        self.wait_for_element(OrderPageLocators.MAIN_HEADER)

    @allure.step('Проверить отображение заголовка главной страницы')
    def check_displaying_main_header(self):
        return self.wait_for_element(OrderPageLocators.MAIN_HEADER)

    @allure.step('Подождать перехода на страницу "Дзен')
    def wait_and_get_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))
        return self.driver.current_url

    @allure.step('Получить переход на страницу "Дзен')
    def check_transition_page_dzen(self):
        expected_url = "https://dzen.ru/?yredirect=true"
        actual_url = self.driver.current_url
        return actual_url == expected_url
