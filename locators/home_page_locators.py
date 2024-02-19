from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGIN_ACCOUNT_LOCATOR = By.XPATH, '//*[contains(text(), "Войти в аккаунт")]'  # кнопка «Войти в аккаунт» на главной странице
    ACCOUNT_BUTTON_LOCATOR = By.XPATH, '//*[contains(text(), "Личный Кабинет")]'  # кнопка "Личный кабинет" на главной странице
    DESIGNER_BUTTON_LOCATOR = By.XPATH, '//*[contains(text(), "Конструктор")]'  # кнопка "Конструктор" на главной странице
    ORDERS_FEED_LOCATOR = By.XPATH, '//*[contains(text(), "Лента Заказов")]'  # кнопка "Лента Заказов" на главной странице
    PLACE_ORDER_BUTTON_LOCATOR = By.XPATH, '//*[contains(text(), "Оформить заказ")]'  # кнопка "Оформить заказ" на главной странице
    INGREDIENT_LOCATOR = By.XPATH, '//*[contains(text(), "Флюоресцентная булка R2-D3")]'  # "Флюоресцентная булка" на главной странице
    POP_UP_WINDOW_LOCATOR = By.XPATH, '//*[contains(@class, "Modal_modal__contentBox__sCy8X pt-10 pb-15")]'  # всплывающее окно при нажатии на ингредиент
    TEXT_INGREDIENT_LOCATOR = By.XPATH, '//*[contains(text(), "Детали ингредиента")]'  # текст "Детали ингрединта" на попапе
    BUTTON_CLOSE_LOCATOR = By.XPATH, '//*[@type="button" and @class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'  # кнопка "Крестик" на попапе
    HOME_PAGE_LOCATOR = By.XPATH, '//*'  # главная страница
    DRAG_DOWN_LOCATOR = By.XPATH, '//*[@class="constructor-element__text"]'  # конструктор перетаскивания ингредиента
    COUNTER_LOCATOR = By.XPATH, '//*[@class="counter_counter__num__3nue1"]'  # счетчик добавление ингредиента
    MODAL_CONTENT_LOCATOR = By.XPATH, '//*[contains(@class, "Modal_modal__contentBox__sCy8X pt-30 pb-30")]'  # всплывающее окно с номером заказа
