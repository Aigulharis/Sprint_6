import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


@pytest.mark.parametrize('question_number', range(1, 9))
def test_question_answer_visibility(driver, question_number):
    main_page = MainPage(driver)
    main_page.scroll_to_important_questions()
    main_page.wait_visibility_of_lines_items(question_number)
    main_page.click_on_element(MainPageLocators.QUESTION_LINE[question_number])# Клик по вопросу (стрелочке)
    answer_locator = MainPageLocators.ANSWER_LANE[question_number] # Подождать, пока ответ станет видимым
    answer_element = main_page.wait_for_element(answer_locator)
    # Проверяем, что ответ содержимое текста не пустое
    text = answer_element.text
    assert text != '', f"Ответ для вопроса {question_number} не отображается или пустой"
