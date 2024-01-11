from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    PLACEHOLDER_EMAIL_LOCATOR = By.XPATH, '//*[contains(@class, "input__placeholder text noselect text_type_main-default")]'  # плейсхолдер 'Email' на странице 'Восстановление пароля'
    BUTTON_PASSWORD_RECOVERY_LOCATOR = By.XPATH, '//*[contains(text(), "Восстановить")]'  # кнопка 'Восстановить' на странице 'Восстановление пароля'
    FIELD_EMAIL_LOCATOR = By.XPATH, '//*[@class="text input__textfield text_type_main-default"]'  # поле для ввода Email
    BUTTON_FOCUSED_LOCATOR = By.XPATH, '//*[contains(@class,"input__icon input__icon-action")]'  # кнопка показать/скрыть пароль
    FOCUSED_FIELD_LOCATOR = By.XPATH, '//*[contains(@class,"input__placeholder-focused")]'  # активное поле "Пароль" после клика на иконку "Глаз"
