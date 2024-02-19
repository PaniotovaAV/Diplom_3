import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from urls import *


class TestHomePage:

    @allure.title('Переход по клику на страницу "Лента Заказов"')
    @allure.description('При нажатии на кнопку "Лента Заказов", происходит переход на страницу заказов')
    def test_orders_feed(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.loading_home_page()
        assert home_page.base_check_orders_feed() == URL_ORDERS_FEED

    @allure.title('Переход по клику на "Конструктор"')
    @allure.description('При нажатии на кнопку "Конструктор", происходит переход на главную страницу')
    def test_designer(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.base_check_orders_feed()
        assert home_page.base_check_designer() == URL_HOME_PAGE

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Проверяем,что на всплывающем окне с детали есть текст "Детали ингредиента"')
    def test_pop_up_window(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.loading_home_page()
        home_page.base_check_orders_feed()
        home_page.base_check_designer()
        assert 'Детали ингредиента' in home_page.base_check_pop_up_window()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    @allure.description('При нажатии на крестик, всплывающее окно закрывается и текст "Детали ингредиента" пропадает')
    def test_close_pop_up_window(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.base_check_orders_feed()
        home_page.base_check_designer()
        home_page.base_check_pop_up_window()
        assert 'Детали ингредиента' not in home_page.base_check_close_pop_up_window()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    @allure.description('После добавления ингредиента в заказ, счётчик ингредиента равен 2')
    def test_close_pop_up_window(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.base_check_orders_feed()
        assert home_page.base_check_drag_and_drop() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('Проверяем, что после успешного входа в аккаунт, пользователь может создать заказ и '
                        'увидеть надпись "Ваш заказ начали готовить"')
    def test_checkout(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.base_check_orders_feed()
        home_page.base_check_drag_and_drop()
        assert 'Ваш заказ начали готовить' in home_page.base_check_text_order()
