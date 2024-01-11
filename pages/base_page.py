from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def loading_page(self, URL):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_contains(URL))

    def find__element_text(self, locator):
        return self.driver.find_element(*locator).text

    def find__element(self, locator):
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    def set_data_to_element(self, locator, data):
        self.driver.find_element(*locator).send_keys(f'{data}')

    def current__url(self):
        return self.driver.current_url

    def wait_element_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))

    def wait_element_located_to_be_selected(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.element_located_to_be_selected(locator))

    def drag_and_drop(self, locator_1, locator_2):
        element = self.driver.find_element(*locator_1)
        target = self.driver.find_element(*locator_2)
        action_chains = ActionChains(self.driver)
        return action_chains.drag_and_drop(element, target).perform()

    def wait_element_(self, locator, text_value):
        return WebDriverWait(self.driver, 15).until(expected_conditions.none_of(
            expected_conditions.text_to_be_present_in_element(locator, text_value)))

    def wait_visibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
    def wait_presence_of_element_located(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))
