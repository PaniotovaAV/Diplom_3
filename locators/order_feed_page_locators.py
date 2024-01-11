from selenium.webdriver.common.by import By


class OrderFeedLocators:
    INGREDIENT_LOCATOR = By.XPATH, '//*//li[1]/a/h2'  # самый верхний заказ на странице "Лента Заказов"
    MODAL_WINDOW_LOCATOR = By.XPATH, '//*[contains(@class, "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10")]'  # всплывающее окно с деталями на странице "Лента Заказов"
    NUM_ORDERS_HISTORY_ORDERS_LOCATOR = By.XPATH, '//*[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]'  # номер заказа на странице "История заказов"
    NUM_ORDERS_FEED_ORDER_LOCATOR = By.XPATH, '//*[@class="OrderFeed_list__OLh59"]'  # номера заказов на странице "Лента заказов"
    NUMBER_ORDERS_LOCATOR = By.XPATH, '//*[@class ="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'  # номер нового заказа на главной странице
    DONE_ORDERS_ALL_TIME_LOCATOR = By.XPATH, '//p[contains(text(),"Выполнено за все время")]/following-sibling::p[contains(@class, "OrderFeed_number")]'  # количество заказов выполненных за все время на странице "Лента заказов"
    DONE_ORDERS_TODAY_LOCATOR = By.XPATH, '//p[contains(text(),"Выполнено за сегодня")]/following-sibling::p[contains(@class, "OrderFeed_number")]'  # количество заказов выполненных за сегодня на странице "Лента заказов"
    LOGO_BUTTON_LOCATOR = By.XPATH, '//*[@class="AppHeader_header__logo__2D0X2"]'  # логотип "Stellar Burgers"
    NUM_ORDER_IN_WORK_LOCATOR = By.XPATH, '//p[contains(text(), "В работе")]/following-sibling::ul[2]/li'  # номер после оформления заказа в разделе "В работе"
