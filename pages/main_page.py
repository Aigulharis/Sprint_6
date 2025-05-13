import allure
from locators.main_page_locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    @allure.step('Проскроллить до раздела "Вопросы о важном"')
    def scroll_to_important_questions(self):
        self.scroll_to_element(MainPageLocators.IMPORTANT_QUESTIONS)

    @allure.step('Подождать загрузки номера вопроса в разделе "Вопросы о важнoм"')
    def wait_visibility_of_lines_items(self, data):
        self.wait_for_element(MainPageLocators.QUESTION_LINE[data])

    @allure.step('Кликнуть на нужный номер вопроса в аккордеоне "Вопросы о важнoм"')
    def click_on_lines_items(self, data):
        self.click_on_element(MainPageLocators.QUESTION_LINE[data])

    @allure.step('Подождать загрузки нужного номера ответа в разделе "Вопросы о важнoм"')
    def wait_visibility_of_answer_lane(self, data):
        self.wait_for_element(MainPageLocators.ANSWER_LANE[data])

    @allure.step('Получить текст нужного номера ответа в разделе "Вопросы о важнoм"')
    def get_displayed_text_from_answer_lane(self, data):
        return self.get_text_on_element(MainPageLocators.ANSWER_LANE[data])
