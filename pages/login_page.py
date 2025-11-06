from selenium.webdriver.common.by import By
import allure

from core.urls import LOGIN_PAGE_URL
from pages.base_page import BasePage
from pages.components import HeaderComponent


class LoginPage(BasePage):
    
    BUTTON_FORGOT_PASSWORD = (By.XPATH, "//*[@href='/forgot-password']")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver)

    @allure.step(f'Открыть страницу {LOGIN_PAGE_URL}')
    def open(self):
        super().open(LOGIN_PAGE_URL)

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_button_recover_password(self):
        self.click(self.BUTTON_FORGOT_PASSWORD)

    @allure.step(f'Проверить, что url страницы: {LOGIN_PAGE_URL}')
    def check_url_is_login_page(self):
        return self.check_url_is(LOGIN_PAGE_URL)

    
    