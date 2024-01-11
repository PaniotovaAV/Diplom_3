import allure
from data import *
from pages.profile_page import ProfilePage


class TestProfilePage:
    @allure.title('Переход по клику на "Личный кабинет"')
    @allure.description('При нажатии на кнопку "Личный кабинет", происходит переход на страницу профиля')
    def test_profile(self, driver):
        assert ProfilePage(driver).base_check_profile() == URL_ACCOUNT_PROFILE

    @allure.title('Переход в раздел "История заказов" в личном кабинете')
    @allure.description('При нажатии на кнопку "История заказов", происходит переход на страницу истории заказов')
    def test_order_history(self, driver):
        assert ProfilePage(driver).base_check_order_history() == URL_ORDER_HISTORY

    @allure.title('Выход из аккаунта')
    @allure.description('При нажатии на кнопку "Выход", происходит переход на страницу регистрации')
    def test_logout(self, driver):
        assert ProfilePage(driver).base_check_logout() == URL_LOGIN_PAGE
