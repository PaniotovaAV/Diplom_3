import allure
from locators.profile_page_locators import ProfileLocators
from pages.base_page import BasePage
from urls import *


class ProfilePage(BasePage):

    @allure.step('Ожидаем загрузку страницы "Личный кабинет"')
    def loading_account_profile_page(self):
        return self.loading_page(URL_ACCOUNT_PROFILE)

    @allure.step('Ожидаем загрузку страницы "История заказов"')
    def loading_history_page(self):
        return self.loading_page(URL_ORDER_HISTORY)

    @allure.step('Нажимаем на кнопку "История заказов" в личном кабинете')
    def click_button_order_history(self):
        locator = ProfileLocators.ORDER_HISTORY_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Находим кнопку "История заказов" в личном кабинете')
    def find_button_order_history(self):
        locator = ProfileLocators.ORDER_HISTORY_LOCATOR
        return self.find__element(locator)

    @allure.step('Ожидаем наличие кнопки "История заказов" в личном кабинете')
    def wait_visibility_button_order_history(self):
        locator = ProfileLocators.ORDER_HISTORY_LOCATOR
        return self.wait_visibility_of_element_located(locator)

    @allure.step('Нажимаем на кнопку "Выйти" в личном кабинете')
    def click_button_logout(self):
        locator = ProfileLocators.LOGOUT_BUTTON_LOCATOR
        self.wait_visibility_of_element_located(locator)
        return self.click_to_element(locator)

    @allure.step('Ожидаем кликабельность кнопки "Выйти" в личном кабинете')
    def wait_clickable_logout_button(self):
        locator = ProfileLocators.LOGOUT_BUTTON_LOCATOR
        return self.wait_element_clickable(locator)

    @allure.step('Общие шаги для перехода в "Личный кабинет"')
    def base_check_profile(self):
        self.loading_page(URL_ACCOUNT_PROFILE)
        return self.current__url()

    @allure.step('Общие шаги для перехода в раздел "История заказов" в личном кабинете')
    def base_check_order_history(self):
        self.loading_page(URL_ACCOUNT_PROFILE)
        self.wait_clickable_logout_button()
        self.find_button_order_history()
        self.click_button_order_history()
        self.loading_page(URL_ORDER_HISTORY)
        return self.current__url()

    @allure.step('Общие шаги выхода из аккаунта')
    def base_check_logout(self):
        self.loading_page(URL_ACCOUNT_PROFILE)
        self.wait_clickable_logout_button()
        self.click_button_logout()
        self.loading_page(URL_LOGIN_PAGE)
        return self.current__url()

    @allure.step('Общие шаги для нажатия на кнопку "История заказов"')
    def base_check_click_button_order_history(self):
        self.wait_visibility_button_order_history()
        self.find_button_order_history()
        self.click_button_order_history()

    @allure.step('Общие шаги для перехода между страницами "Профиль" и "История заказов"')
    def base_check_switch_over_account_profile_and_history_pages(self):
        self.loading_account_profile_page()
        self.base_check_click_button_order_history()
        self.loading_history_page()
