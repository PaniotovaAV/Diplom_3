import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями на странице "Лента Заказов"')
    @allure.description('При нажатии на заказ, открывается всплывающее окно с деталями заказа')
    def test_order_pop_up_window(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.base_check_orders_feed()
        assert 'Выполнен' in order_feed_page.base_check_orders_feed_pop_up_window()

    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    @allure.description('Проверяем, что после созданного заказа, его номер отображается на странице "Лента Заказов" и '
                        'в разделе личного кабинета "История заказов"')
    def test_order_user_history_and_order_feed(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.base_check_checkout()
        number_order = order_feed_page.base_check_number_new_order()
        home_page.base_check_click_button_close_and_orders_feed()
        text_order_feed = order_feed_page.base_check_find_num_orders_feed_order()
        home_page.base_check_click_button_account()
        profile_page.base_check_switch_over_account_profile_and_history_pages()
        text_order_history = order_feed_page.base_check_num_order_history_orders()
        assert f'{number_order}' in f'{text_order_feed}' and f'{number_order}' in f'{text_order_history}'

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description('Проверяем, что после созданного заказа,'
                        'на странице "Лента Заказов" в счётчике "Выполнено за всё время" количество заказов увеличивается на 1')
    def test_rise_num_orders_all_time(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.base_check_click_orders_feed()
        last_count_order = order_feed_page.base_check_last_count_orders_all_time()
        order_feed_page.base_check_click_logo()
        home_page.base_check_checkout()
        order_feed_page.wait__element_number_orders()
        order_feed_page.find_number_orders()
        new_num_order = order_feed_page.new_num_order()
        home_page.base_check_click_button_close()
        assert int(last_count_order) + 1 == int(new_num_order)

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description('Проверяем, что после созданного заказа,'
                        'на странице "Лента Заказов" в счётчике "Выполнено за сегодня" количество заказов увеличивается на 1')
    def test_rise_num_orders_today(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.base_check_click_orders_feed()
        last_count_order_today = order_feed_page.base_check_last_count_orders_today()
        order_feed_page.base_check_click_logo()
        home_page.base_check_checkout()
        home_page.base_check_click_button_close_and_orders_feed()
        new_count_order_today = order_feed_page.base_check_rise_num_orders_today()
        assert int(new_count_order_today) - int(last_count_order_today) == 1

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    @allure.description('Проверяем, что после созданного заказа, '
                        'его номер равен номеру заказа в разделе "В работе" на странице "Лента Заказов"')
    def test_num_order_in_work(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page.base_check_loading_home_page()
        login_page.base_check_login()
        home_page.base_check_checkout()
        number_order = order_feed_page.base_check_number_new_order()
        home_page.base_check_click_button_close_and_orders_feed()
        num_order_in_work = order_feed_page.base_check_number_order_in_work()
        assert f'0{number_order}' == f'{num_order_in_work}'
