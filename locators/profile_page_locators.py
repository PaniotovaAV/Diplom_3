from selenium.webdriver.common.by import By


class ProfileLocators:
    ORDER_HISTORY_LOCATOR = By.XPATH, '//*[contains(text(), "История заказов")]'  # кнопка "История заказов" в личном кабинете
    LOGOUT_BUTTON_LOCATOR = By.XPATH, '//*[contains(text(), "Выход")]'  # кнопка "Выйти" в личном кабинете
