from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Страница заполнения данных "Для кого самокат"
    TITLE_PAGE_FILL_PERSONAL_INFO = (By.XPATH, ".//div[text()='Для кого самокат']")
    INPUT_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    INPUT_LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    SELECT_ITEM_METRO = (By.XPATH, ".//li[@class='select-search__row']")
    INPUT_PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    FURTHER_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    # Страница заполнения данных "Про аренду"
    TITLE_PAGE_ABOUT_RENT = (By.XPATH, ".//div[text()='Про аренду']")
    INPUT_WHEN_BRING = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    CALENDAR = (By.XPATH, ".//div[@class='react-datepicker-popper']")
    CALENDAR_ELEMENT = (By.XPATH, ".//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]")
    INPUT_RENTAL_PERIOD = (By.XPATH, ".//div[@aria-haspopup='listbox' and .//div[text()='* Срок аренды']]")
    DROPDOWN_LIST_RENTAL_PERIOD = (By.XPATH, ".//div[@role='option' and text()='трое суток']")
    CHECKBOX_COLOR_SCOOTER_BLACK = (By.XPATH, ".//input[@id='black']")
    CHECKBOX_COLOR_SCOOTER_GREY = (By.XPATH, ".//input[@id='grey']")
    INPUT_COMMENT_COURIER = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(.//button[text()='Заказать'])[2]")

    # Форма подтверждения
    ORDER_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    # Форма заказ оформлен
    WATCH_STATUS_BUTTON = (By.XPATH, ".// button[text() = 'Посмотреть статус']")
    # Страница данных о заказе
    ORDER_INFORMATION_PAGE = (By.XPATH, ".//div[contains(text(), 'Самокат на складе')]")


    # Логотип Яндекса
    LOGO_YANDEX = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex') and @href='//yandex.ru']")
    # Логотип Самоката
    LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']")
    # Заголовок на главной странице
    MAIN_HEADER = (By.XPATH, ".//div[contains(@class, 'Home_Header__iJKdX')]")
