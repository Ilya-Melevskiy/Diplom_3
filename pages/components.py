from selenium.webdriver.common.by import By
import allure

from pages.base_page import BasePage


class HeaderPage(BasePage):

    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//a[@href='/account']")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    BUTTON_ORDERS_FEED = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на "Личный кабинет"')
    def click_button_personal_account(self):
        self.click(self.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Клик на "Лента Заказов"')
    def click_button_orders_feed(self):
        self.click(self.BUTTON_ORDERS_FEED)

    @allure.step('Клик на "Конструктор"')
    def click_button_constructor(self):
        self.click(self.BUTTON_CONSTRUCTOR)

    
    