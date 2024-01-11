import allure
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями на странице "Лента Заказов"')
    @allure.description('При нажатии на заказ, открывается всплывающее окно с деталями заказа')
    def test_order_pop_up_window(self, driver):
        assert 'Выполнен' in OrderFeedPage(driver).base_check_orders_feed_pop_up_window()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_user_history_and_order_feed(self, driver):
        num_order = OrderFeedPage(driver).base_check_order_user_history_and_order_feed()
        assert f'{num_order[0]}' in f'{num_order[1]}' and f'{num_order[0]}' in f'{num_order[2]}'

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_rise_num_orders_all_time(self, driver):
        result = OrderFeedPage(driver).base_check_rise_num_orders_all_time()
        assert int(result[0]) + 1 == int(result[1])

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_rise_num_orders_today(self, driver):
        result = OrderFeedPage(driver).base_check_rise_num_orders_today()
        assert int(result[1]) - int(result[0]) == 1

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_num_order_in_work(self, driver):
        result = OrderFeedPage(driver).base_check_number_order_in_work()
        assert f'0{result[0]}' == f'{result[1]}'
