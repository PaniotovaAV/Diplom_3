import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from urls import *


class TestProfilePage:
    @allure.title('Переход по клику на "Личный кабинет"')
    @allure.description('При нажатии на кнопку "Личный кабинет", происходит переход на страницу профиля')
    def test_profile(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.loading_home_page()
        home_page.click_button_account()
        assert profile_page.base_check_profile() == URL_ACCOUNT_PROFILE

    @allure.title('Переход в раздел "История заказов" в личном кабинете')
    @allure.description('При нажатии на кнопку "История заказов", происходит переход на страницу истории заказов')
    def test_order_history(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.loading_home_page()
        home_page.click_button_account()
        profile_page.base_check_profile()
        assert profile_page.base_check_order_history() == URL_ORDER_HISTORY

    @allure.title('Выход из аккаунта')
    @allure.description('При нажатии на кнопку "Выход", происходит переход на страницу регистрации')
    def test_logout(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.loading_home_page()
        home_page.click_button_account()
        profile_page.base_check_profile()
        assert profile_page.base_check_logout() == URL_LOGIN_PAGE
