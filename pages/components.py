from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.base_page import BasePage


class HeaderComponent():

    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//a[@href='/account']")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    BUTTON_ORDERS_FEED = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")

    def __init__(self, driver): 
        self.driver = driver 

    def wait_visibility(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def wait_invisibility(self, locator):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))

    def wait_overlay_invisibility(self):
        self.wait_invisibility(BasePage.OVERLAY)
        self.wait_invisibility(BasePage.OVERLAY_2)
    
    def wait_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    def find_element(self, locator): 
        self.wait_visibility(locator)
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.wait_overlay_invisibility()
        self.wait_clickable(locator)
        self.find_element(locator).click()

    @allure.step('Клик на "Личный кабинет"')
    def click_button_personal_account(self):
        self.click(self.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Клик на "Лента Заказов"')
    def click_button_orders_feed(self):
        self.click(self.BUTTON_ORDERS_FEED)

    @allure.step('Клик на "Конструктор"')
    def click_button_constructor(self):
        self.click(self.BUTTON_CONSTRUCTOR)

    
    