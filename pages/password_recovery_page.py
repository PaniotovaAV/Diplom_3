import allure
from data import *
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage


class PasswordRecoveryPage(BasePage):

    @allure.step('Нажимаем на плейсхолдер "Email" на странице "Восстановление пароля"')
    def click_email_placeholder(self):
        locator = PasswordRecoveryPageLocators.PLACEHOLDER_EMAIL_LOCATOR
        return self.click_to_element(locator)

    @allure.step('Вводим email зарегистрированного пользователя')
    def input_email_user(self):
        locator = PasswordRecoveryPageLocators.FIELD_EMAIL_LOCATOR
        return self.set_data_to_element(locator, LoginPage.user_login(self))

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_button_password_recovery(self):
        locator = PasswordRecoveryPageLocators.BUTTON_PASSWORD_RECOVERY_LOCATOR
        return self.click_to_element(locator)

    @allure.step('Нажимаем на кнопку показать/скрыть пароль')
    def click_button_focused(self):
        locator = PasswordRecoveryPageLocators.BUTTON_FOCUSED_LOCATOR
        return self.click_to_element(locator)

    @allure.step('Поиск подсвеченного поля после нажатия на кнопку показать/скрыть пароль')
    def find_button_focused(self):
        locator = PasswordRecoveryPageLocators.FOCUSED_FIELD_LOCATOR
        return self.find__element(locator)

    @allure.step('Общие шаги для перехода по ссылке "Восстановить пароль" на странице регистрация')
    def base_check_forgot_password(self):
        self.loading_page(URL_HOME_PAGE)
        HomePage.click_login_account(self)
        self.loading_page(URL_LOGIN_PAGE)
        LoginPage.click_restore_password(self)
        return self.current__url()

    @allure.step('Общие шаги на странице "Восстановление пароля"')
    def base_check_reset_password(self):
        self.base_check_forgot_password()
        self.click_email_placeholder()
        self.input_email_user()
        self.click_button_password_recovery()
        self.loading_page(URL_RESET_PASSWORD)
        return self.current__url()

    @allure.step('Общие шаги для клика по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def base_check_active_field_password(self):
        self.base_check_reset_password()
        self.click_button_focused()
        result = self.find_button_focused()
        return result.get_attribute("class")
