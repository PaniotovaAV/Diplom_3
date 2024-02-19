import allure
from data import *
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import *


class LoginPage(BasePage):
    @allure.step('Ожидаем загрузку страницы авторизации')
    def loading_login_page(self):
        return self.loading_page(URL_LOGIN_PAGE)

    @allure.step('Нажимаем на ссылку "Восстановить пароль" на странице регистрации')
    def click_restore_password(self):
        locator = LoginPageLocators.RESTORE_PASSWORD_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Нажимаем на поле "Email" на странице авторизации')
    def click_email(self):
        locator = LoginPageLocators.EMAIL_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Вводим email зарегистрированного пользователя на странице авторизации')
    def set_email(self):
        locator = LoginPageLocators.EMAIL_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.set_data_to_element(locator, EMAIL_USER)

    @allure.step('Нажимаем на поле "Пароль" на странице авторизации')
    def click_password(self):
        locator = LoginPageLocators.PASSWORD_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Вводим пароль зарегистрированного пользователя на странице авторизации')
    def set_password(self):
        locator = LoginPageLocators.PASSWORD_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.set_data_to_element(locator, PASSWORD_USER)

    @allure.step('Ожидаем кнопку "Войти" на странице авторизации')
    def wait_clickable_login_button(self):
        locator = LoginPageLocators.LOGIN_BUTTON_LOCATOR
        return self.wait_element_clickable(locator)

    @allure.step('Нажимаем на кнопку "Войти" на странице авторизации')
    def click_button_enter(self):
        locator = LoginPageLocators.LOGIN_BUTTON_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Общие шаги для авторизации')
    def base_check_login(self):
        self.loading_login_page()
        self.click_email()
        self.set_email()
        self.click_password()
        self.set_password()
        self.wait_clickable_login_button()
        self.click_button_enter()

    @allure.step('Общие шаги для загрузки страницы авторизации и нажатия на ссылку "Восстановить пароль"')
    def base_check_loading_login_page_and_click_restore_password(self):
        self.loading_login_page()
        self.click_restore_password()
