import allure
from data import *
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage


class HomePage(BasePage):
    @allure.step('Нажимаем на кнопку "Войти в аккаунт" на главной странице')
    def click_login_account(self):
        locator = HomePageLocators.LOGIN_ACCOUNT_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Нажимаем на кнопку "Конструктор" на главной странице')
    def click_designer(self):
        locator = HomePageLocators.DESIGNER_BUTTON_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Нажимаем на кнопку "Лента Заказов" на главной странице')
    def click_orders_feed(self):
        locator = HomePageLocators.ORDERS_FEED_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Нажимаем на кнопку "Личный кабинет" на главной странице')
    def click_button_account(self):
        locator = HomePageLocators.ACCOUNT_BUTTON_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Находим кнопку "Личный кабинет" на главной странице')
    def find_button_account(self):
        locator = HomePageLocators.ACCOUNT_BUTTON_LOCATOR
        return self.find__element(locator)

    @allure.step('Ожидаем нахождение кнопки "Личный кабинет" на главной странице')
    def wait_visibility_button_account(self):
        locator = HomePageLocators.ACCOUNT_BUTTON_LOCATOR
        return self.wait_visibility_of_element_located(locator)

    @allure.step('Нажимаем на ингредиент "Флюоресцентная булка" на главной странице')
    def click_button_ingredient(self):
        locator = HomePageLocators.INGREDIENT_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Получаем детали на всплывающем окне')
    def text_pop_up_window(self):
        locator = HomePageLocators.POP_UP_WINDOW_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element_text(locator)

    @allure.step('Закрываем всплывающее окно')
    def click_button_close(self):
        locator = HomePageLocators.BUTTON_CLOSE_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Находим текст на главной странице')
    def text_home_page(self):
        locator = HomePageLocators.HOME_PAGE_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element_text(locator)

    @allure.step('Перетаскиваем ингредиент в заказ')
    def drag__and__drop(self):
        locator_1 = HomePageLocators.INGREDIENT_LOCATOR
        self.wait_visibility_of_element_located(locator_1)
        locator_2 = HomePageLocators.DRAG_DOWN_LOCATOR
        self.wait_visibility_of_element_located(locator_2)
        return self.drag_and_drop(locator_1, locator_2)

    @allure.step('Находим значение счётчика ингредиента, добавленного в заказ')
    def find_element_counter(self):
        locator = HomePageLocators.COUNTER_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element_text(locator)

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_button_checkout(self):
        locator = HomePageLocators.PLACE_ORDER_BUTTON_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Находим кнопку "Оформить заказ"')
    def find_button_checkout(self):
        locator = HomePageLocators.PLACE_ORDER_BUTTON_LOCATOR
        return self.find__element(locator)

    @allure.step('Ожидаем нахождение кнопки "Оформить заказ"')
    def wait_visibility_button_checkout(self):
        locator = HomePageLocators.PLACE_ORDER_BUTTON_LOCATOR
        return self.wait_visibility_of_element_located(locator)

    @allure.step('Получаем текст всплывающего окна, после оформления заказа')
    def text_model_order(self):
        locator = HomePageLocators.MODAL_CONTENT_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element_text(locator)

    @allure.step('Ожидаем появление кнопки "Лента Заказов"')
    def wait_visibility_orders_feed(self):
        locator = HomePageLocators.ORDERS_FEED_LOCATOR
        return self.wait_visibility_of_element_located(locator)

    @allure.step('Ожидаем кликабельность кнопки "Лента Заказов"')
    def wait_clickable_orders_feed(self):
        locator = HomePageLocators.ORDERS_FEED_LOCATOR
        return self.wait_element_clickable(locator)

    @allure.step('Ожидаем кликабельность кнопки "Войти в аккаунт"')
    def wait_clickable_login_account(self):
        locator = HomePageLocators.LOGIN_ACCOUNT_LOCATOR
        return self.wait_element_clickable(locator)

    @allure.step('Находим кнопку "Крестик" на всплывающем окне')
    def find_button_close(self):
        locator = HomePageLocators.BUTTON_CLOSE_LOCATOR
        return self.find__element(locator)

    @allure.step('Ожидаем появление кнопки "Крестик" на всплывающем окне')
    def wait_visibility_button_close(self):
        locator = HomePageLocators.BUTTON_CLOSE_LOCATOR
        return self.wait_visibility_of_element_located(locator)

    @allure.step('Находим кнопку "Лента Заказов"')
    def find_orders_feed(self):
        locator = HomePageLocators.ORDERS_FEED_LOCATOR
        return self.find__element(locator)

    @allure.step('Ожидаем кликабельность нажатия на "Флюоресцентная булка"')
    def wait_clickable_ingredient(self):
        locator = HomePageLocators.INGREDIENT_LOCATOR
        return self.wait_element_clickable(locator)

    @allure.step('Ожидаем кликабельность всплывающего окна при нажатии на ингредиент')
    def wait_clickable_pop_up_window(self):
        locator = HomePageLocators.POP_UP_WINDOW_LOCATOR
        return self.wait_element_clickable(locator)

    @allure.step('Проверка присутствия кнопки "Крестик" на всплывающем окне')
    def wait_presence_button_close(self):
        locator = HomePageLocators.BUTTON_CLOSE_LOCATOR
        return self.wait_visibility_of_element_located(locator)

    @allure.step('Проверка кликабельности кнопки "Крестик" на всплывающем окне')
    def wait_clickable_button_close(self):
        locator = HomePageLocators.BUTTON_CLOSE_LOCATOR
        return self.wait_element_clickable(locator)

    @allure.step('Общие шаги для авторизации')
    def base_check_login(self):
        self.loading_page(URL_HOME_PAGE)
        self.wait_clickable_login_account()
        HomePage.click_login_account(self)
        self.loading_page(URL_LOGIN_PAGE)
        LoginPage.click_email(self)
        LoginPage.set_email(self)
        LoginPage.click_password(self)
        LoginPage.set_password(self)
        LoginPage.wait_clickable_login_button(self)
        LoginPage.click_button_enter(self)
        self.loading_page(URL_HOME_PAGE)

    @allure.step('Общие шаги для перехода в раздел "Лента Заказов"')
    def base_check_orders_feed(self):
        self.base_check_login()
        self.wait_clickable_orders_feed()
        self.click_orders_feed()
        self.loading_page(URL_ORDERS_FEED)
        return self.current__url()

    @allure.step('Общие шаги для перехода в раздел  "Конструктор"')
    def base_check_designer(self):
        self.base_check_orders_feed()
        self.click_designer()
        self.loading_page(URL_HOME_PAGE)
        return self.current__url()

    @allure.step('Общие шаги для появления всплывающего окна при нажатии на ингредиент')
    def base_check_pop_up_window(self):
        self.base_check_designer()
        self.loading_page(URL_HOME_PAGE)
        self.wait_clickable_ingredient()
        self.click_button_ingredient()
        self.wait_clickable_pop_up_window()
        return self.text_pop_up_window()

    @allure.step('Общие шаги для закрытия всплывающего окна')
    def base_check_close_pop_up_window(self):
        self.base_check_pop_up_window()
        self.click_button_close()
        self.loading_page(URL_HOME_PAGE)
        return self.text_home_page()

    @allure.step('Общие шаги для перетаскивания ингредиента в заказ')
    def base_check_drag_and_drop(self):
        self.base_check_orders_feed()
        self.click_designer()
        self.loading_page(URL_HOME_PAGE)
        self.drag__and__drop()
        return self.find_element_counter()

    @allure.step('Общие шаги получения номера заказа зарегистрированного пользователя')
    def base_check_checkout(self):
        self.base_check_drag_and_drop()
        self.click_button_checkout()
        return self.text_model_order()
