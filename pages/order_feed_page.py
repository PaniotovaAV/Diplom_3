import allure
from locators.order_feed_page_locators import OrderFeedLocators
from pages.base_page import BasePage
from urls import *


class OrderFeedPage(BasePage):

    @allure.step('Нажимаем на заказ на странице "Лента Заказов"')
    def click_order(self):
        locator = OrderFeedLocators.INGREDIENT_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Получаем текст всплывающего окна заказа на странице "Лента Заказов"')
    def text_order(self):
        locator = OrderFeedLocators.MODAL_WINDOW_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element_text(locator)

    @allure.step('Получаем номера заказов на странице "История заказов"')
    def num_order_history_orders(self):
        locator = OrderFeedLocators.NUM_ORDERS_HISTORY_ORDERS_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element_text(locator)

    @allure.step('Получаем номера заказов на странице "Лента заказов"')
    def num_order_feed_order(self):
        locator = OrderFeedLocators.NUM_ORDERS_FEED_ORDER_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element_text(locator)

    @allure.step('Находим номер нового заказа на главной странице')
    def find_new_num_order(self):
        locator = OrderFeedLocators.NUMBER_ORDERS_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element(locator)

    @allure.step('Получаем номер нового заказа на главной странице')
    def new_num_order(self):
        locator = OrderFeedLocators.NUMBER_ORDERS_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element_text(locator)

    @allure.step('Ожидание появления нового номера заказов')
    def wait__element_number_orders(self):
        locator = OrderFeedLocators.NUMBER_ORDERS_LOCATOR
        text_value = self.find__element_text(locator)
        return self.wait_element_(locator, text_value)

    @allure.step('Находим счетчик заказов "Выполнено за все время" на странице "Лента Заказов"')
    def find_num_order_all_time(self):
        locator = OrderFeedLocators.DONE_ORDERS_ALL_TIME_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element(locator)

    @allure.step('Находим счетчик заказов "Выполнено за все время" на странице "Лента Заказов"')
    def find_num_order_today(self):
        locator = OrderFeedLocators.DONE_ORDERS_TODAY_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element(locator)

    @allure.step('Находим номер после оформления заказа в разделе "В работе"')
    def find_num_order_in_work(self):
        locator = OrderFeedLocators.NUM_ORDER_IN_WORK_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element(locator)

    @allure.step('Получаем счетчик заказов "Выполнено за все время" на странице "Лента Заказов"')
    def num_order_all_time(self):
        locator = OrderFeedLocators.DONE_ORDERS_ALL_TIME_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element_text(locator)

    @allure.step('Получаем счетчик заказов "Выполнено за сегодня" на странице "Лента Заказов"')
    def num_order_today(self):
        locator = OrderFeedLocators.DONE_ORDERS_TODAY_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element_text(locator)

    @allure.step('Получаем номер после оформления заказа в разделе "В работе"')
    def num_order_in_work(self):
        locator = OrderFeedLocators.NUM_ORDER_IN_WORK_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.find__element_text(locator)

    @allure.step('Ожидание появления номера заказов за все время')
    def wait__element_all_time(self):
        locator = OrderFeedLocators.DONE_ORDERS_ALL_TIME_LOCATOR
        text_value = self.find__element_text(locator)
        return self.wait_element_(locator, text_value)

    @allure.step('Ожидание появления номера заказа в разделе "В работе"')
    def wait__element_in_work(self):
        locator = OrderFeedLocators.NUM_ORDER_IN_WORK_LOCATOR
        text_value = self.find__element_text(locator)
        return self.wait_element_(locator, text_value)

    @allure.step('Ожидание присутствие номера заказа в разделе "В работе"')
    def wait_visibility_element_in_work(self):
        locator = OrderFeedLocators.NUM_ORDER_IN_WORK_LOCATOR
        return self.wait_visibility_of_element_located(locator)

    def wait_visibility_element_today(self):
        locator = OrderFeedLocators.DONE_ORDERS_TODAY_LOCATOR
        return self.wait_visibility_of_element_located(locator)

    def wait_visibility_element_all_time(self):
        locator = OrderFeedLocators.DONE_ORDERS_ALL_TIME_LOCATOR
        return self.wait_visibility_of_element_located(locator)

    @allure.step('Нажимаем на логотип "Stellar Burgers"')
    def click_logo(self):
        locator = OrderFeedLocators.LOGO_BUTTON_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Ожидаем видимость номеров заказов на странице "Лента Заказов"')
    def wait_visibility_num_orders_feed_order(self):
        locator = OrderFeedLocators.NUM_ORDERS_FEED_ORDER_LOCATOR
        return self.wait_visibility_of_element_located(locator)

    @allure.step('Ожидаем видимость номеров заказов на странице "История Заказов"')
    def wait_visibility_num_orders_history(self):
        locator = OrderFeedLocators.NUM_ORDERS_HISTORY_ORDERS_LOCATOR
        return self.wait_visibility_of_element_located(locator)

    @allure.step('Находим номера заказов на странице "Лента Заказов"')
    def find_num_orders_feed_order(self):
        locator = OrderFeedLocators.NUM_ORDERS_FEED_ORDER_LOCATOR
        return self.find__element(locator)

    @allure.step('Находим номера заказов на странице "История Заказов"')
    def find_num_orders_history(self):
        locator = OrderFeedLocators.NUM_ORDERS_HISTORY_ORDERS_LOCATOR
        return self.find__element(locator)

    @allure.step('Ожидаем кликабельность логотипа на странице "Лента Заказов"')
    def wait_clickable_logo_button(self):
        locator = OrderFeedLocators.LOGO_BUTTON_LOCATOR
        return self.wait_element_clickable(locator)

    @allure.step('Находим логотип на странице "Лента Заказов"')
    def find_logo_button(self):
        locator = OrderFeedLocators.LOGO_BUTTON_LOCATOR
        return self.find__element(locator)

    @allure.step('Находим номера нового заказов на странице "Лента Заказов"')
    def find_number_orders(self):
        locator = OrderFeedLocators.NUMBER_ORDERS_LOCATOR
        return self.find__element(locator)

    @allure.step('Общие шаги для перехода в раздел "Лента Заказов" и открытия всплывающего окна с деталями')
    def base_check_orders_feed_pop_up_window(self):
        self.loading_page(URL_ORDERS_FEED)
        self.click_order()
        return self.text_order()

    @allure.step('Общие шаги получения номера нового заказа')
    def base_check_number_new_order(self):
        self.wait__element_number_orders()
        self.find_new_num_order()
        number_order = self.new_num_order()
        return number_order

    @allure.step('Общие шаги получения текста страницы "Лента Заказов"')
    def base_check_find_num_orders_feed_order(self):
        self.loading_page(URL_ORDERS_FEED)
        self.wait_visibility_num_orders_feed_order()
        self.find_num_orders_feed_order()
        text_order_feed = self.num_order_feed_order()
        return text_order_feed

    @allure.step('Общие шаги получения текста страницы "История заказов"')
    def base_check_num_order_history_orders(self):
        self.wait_visibility_num_orders_history()
        self.find_num_orders_history()
        text_order_history = self.num_order_history_orders()
        return text_order_history

    @allure.step('Общие шаги: получение количества заказов "Выполнено за всё время"')
    def base_check_last_count_orders_all_time(self):
        self.loading_page(URL_ORDERS_FEED)
        self.wait_visibility_element_all_time()
        self.find_num_order_all_time()
        last_count_order = self.num_order_all_time()
        return last_count_order

    @allure.step('Общие шаги для нажатия на логотип "Stellar Burgers"')
    def base_check_click_logo(self):
        self.wait_clickable_logo_button()
        self.find_logo_button()
        self.click_logo()

    @allure.step('Общие шаги: получение количества заказов "Выполнено за сегодня"')
    def base_check_last_count_orders_today(self):
        self.loading_page(URL_ORDERS_FEED)
        self.wait_visibility_element_today()
        self.find_num_order_today()
        last_count_order_today = self.num_order_today()
        return last_count_order_today

    @allure.step('Общие шаги: при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def base_check_rise_num_orders_today(self):
        self.loading_page(URL_ORDERS_FEED)
        self.find_num_order_today()
        new_count_order_today = self.num_order_today()
        return new_count_order_today

    @allure.step('Общие шаги: после оформления заказа его номер появляется в разделе "В работе"')
    def base_check_number_order_in_work(self):
        self.loading_page(URL_ORDERS_FEED)
        self.wait_visibility_element_in_work()
        self.find_num_order_in_work()
        self.wait__element_in_work()
        num_order_in_work = self.num_order_in_work()
        return num_order_in_work
