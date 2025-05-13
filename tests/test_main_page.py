import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import Data


@pytest.mark.parametrize('question_number, expected_answer', Data.test_data_expected_response)
def test_question_answer_visibility(driver, question_number, expected_answer):
    main_page = MainPage(driver)
    main_page.scroll_to_important_questions()
    main_page.wait_visibility_of_lines_items(question_number) #Ожидаем строку с указанным номером
    main_page.click_on_element(MainPageLocators.QUESTION_LINE[question_number])  # Клик по вопросу (стрелочке)
    answer_locator = MainPageLocators.ANSWER_LANE[question_number]  # Ожидаем появления ответа
    answer_element = main_page.wait_for_element(answer_locator)
    text = answer_element.text # Возврат строки
    assert text == expected_answer #Сравниваем полученный текст с ожидаемым ответом