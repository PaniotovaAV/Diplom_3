import allure
from data import *
from pages.home_page import HomePage


class TestHomePage:
    @allure.title('Переход по клику на страницу "Лента Заказов"')
    @allure.description('При нажатии на кнопку "Лента Заказов", происходит переход на страницу заказов')
    def test_orders_feed(self, driver):
        assert HomePage(driver).base_check_orders_feed() == URL_ORDERS_FEED

    @allure.title('Переход по клику на "Конструктор"')
    @allure.description('При нажатии на кнопку "Конструктор", происходит переход на главную страницу')
    def test_designer(self, driver):
        assert HomePage(driver).base_check_designer() == URL_HOME_PAGE

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_pop_up_window(self, driver):
        assert 'Детали ингредиента' in HomePage(driver).base_check_pop_up_window()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    @allure.description('При нажатии на крестик, всплывающее окно закрывается и текст "Детали ингредиента" пропадает')
    def test_close_pop_up_window(self, driver):
        assert 'Детали ингредиента' not in HomePage(driver).base_check_close_pop_up_window()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    @allure.description('После добавления ингредиента в заказ, счётчик ингредиента равен 2')
    def test_close_pop_up_window(self, driver):
        assert HomePage(driver).base_check_drag_and_drop() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_checkout(self, driver):
        assert 'Ваш заказ начали готовить' in HomePage(driver).base_check_checkout()
