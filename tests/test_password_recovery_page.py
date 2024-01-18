import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from urls import *


class TestPasswordRecoveryPage:
    @allure.title('Переход на страницу "Восстановление пароля" по ссылке "Восстановить пароль" на странице регистрация')
    @allure.description('После успешного нажатия на ссылку "Восстановить пароль", '
                        'произошел переход на страницу "Восстановление пароля"')
    def test_forgot_password(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_loading_login_page_and_click_restore_password()
        assert password_recovery_page.url_forgot_password() == URL_FORGOT_PASSWORD

    @allure.title('Ввод почты и клик по кнопке "Восстановить" на странице "Восстановление пароля"')
    @allure.description('После успешного ввода данных и нажатия на кнопку "Восстановить", '
                        'произошел переход на страницу сброса пароля')
    def test_reset_password(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_loading_login_page_and_click_restore_password()
        password_recovery_page.url_forgot_password()
        assert password_recovery_page.base_check_reset_password() == URL_RESET_PASSWORD

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('При нажатии на кнопку показать/скрыть пароль,'
                        'поле для ввода пароля становится подсвеченным')
    def test_active_field_password(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_loading_login_page_and_click_restore_password()
        password_recovery_page.url_forgot_password()
        password_recovery_page.base_check_reset_password()
        assert 'input__placeholder-focused' in password_recovery_page.base_check_active_field_password()
