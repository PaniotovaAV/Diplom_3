from selenium.webdriver.common.by import By


class LoginPageLocators:
    RESTORE_PASSWORD_LOCATOR = By.XPATH, '//*[contains(text(), "Восстановить пароль")]'  # ссылка "Восстановить пароль" на странице регистрации
    EMAIL_LOCATOR = By.XPATH, '//*[text()="Email"]/following-sibling::input'  # поле "Email" на странице авторизации
    PASSWORD_LOCATOR = By.XPATH, '//*[text()="Пароль"]/following-sibling::input'  # поле "Пароль" на странице авторизации
    LOGIN_BUTTON_LOCATOR = By.XPATH, '//*[contains(@class, "button_button__33qZ0")]'  # кнопка "Войти" на странице авторизации
