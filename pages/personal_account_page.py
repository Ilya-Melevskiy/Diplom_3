from selenium.webdriver.common.by import By
import allure

from pages.base_page import BasePage
from core.urls import PERSONAL_ACCOUNT_PAGE_URL, ORDERS_HISTORY_PAGE_URL


class PersonalAccountPage(BasePage):
    BUTTON_ORDERS_HISTORY = (By.XPATH, "//a[@href='/account/order-history']")
    BUTTON_LOGOUT = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    ID_ORDER = (By.XPATH, "//*[@class='text text_type_digits-default']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step(f'Открыть страницу {PERSONAL_ACCOUNT_PAGE_URL}')
    def open(self):
        super().open(PERSONAL_ACCOUNT_PAGE_URL)

    @allure.step('Клик на "История заказов"')
    def click_orders_history(self):
        self.click(self.BUTTON_ORDERS_HISTORY)

    @allure.step('Клик на кнопку "Выйти"')
    def click_button_logout(self):
        self.click(self.BUTTON_LOGOUT)

    @allure.step(f'Проверить, что url страницы: {PERSONAL_ACCOUNT_PAGE_URL}')
    def check_url_is_personal_account_page(self):
        return self.check_url_is(PERSONAL_ACCOUNT_PAGE_URL)
    
    @allure.step(f'Проверить, что url страницы: {ORDERS_HISTORY_PAGE_URL}')
    def check_url_is_orders_history_page(self):
        return self.check_url_is(ORDERS_HISTORY_PAGE_URL)
    
    @allure.step('Получить список заказов в "Истории заказов"')
    def get_list_orders_history(self):
        elements = self.find_elements(self.ID_ORDER)
        ids_orders_in_orders_history = []
        for element in elements:
            ids_orders_in_orders_history.append(element.text)

        return ids_orders_in_orders_history
        
    

        
