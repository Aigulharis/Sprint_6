from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки "Заказать" на главной странице
    ORDER_BUTTON_MAIN =  (By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']")
    ORDER_BUTTON_MAIN_BELOW = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button")

# Элемент "Вопросы о важном" important questions
    IMPORTANT_QUESTIONS = (By.XPATH, ".//div[text()='Вопросы о важном']")
    #вопросы
    QUESTION_LINE = {
        1: [By.XPATH, ".//div[@id='accordion__heading-0']"],
        2: [By.XPATH, ".//div[@id='accordion__heading-1']"],
        3: [By.XPATH, ".//div[@id='accordion__heading-2']"],
        4: [By.XPATH, ".//div[@id='accordion__heading-3']"],
        5: [By.XPATH, ".//div[@id='accordion__heading-4']"],
        6: [By.XPATH, ".//div[@id='accordion__heading-5']"],
        7: [By.XPATH, ".//div[@id='accordion__heading-6']"],
        8: [By.XPATH, ".//div[@id='accordion__heading-7']"]
    }
    #ответы
    ANSWER_LANE = {
        1: [By.XPATH, ".//div[@id='accordion__panel-0']"],
        2: [By.XPATH, ".//div[@id='accordion__panel-1']"],
        3: [By.XPATH, ".//div[@id='accordion__panel-2']"],
        4: [By.XPATH, ".//div[@id='accordion__panel-3']"],
        5: [By.XPATH, ".//div[@id='accordion__panel-4']"],
        6: [By.XPATH, ".//div[@id='accordion__panel-5']"],
        7: [By.XPATH, ".//div[@id='accordion__panel-6']"],
        8: [By.XPATH, ".//div[@id='accordion__panel-7']"]
    }
