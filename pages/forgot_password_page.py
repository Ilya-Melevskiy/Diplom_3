from selenium.webdriver.common.by import By
import allure

from core.urls import FORGOT_PASSWORD_PAGE_URL, RESET_PASSWORD_PAGE_URL
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    INPUT_EMAIL = (By.XPATH, "//*[@class= 'text input__textfield text_type_main-default']")
    BUTTON_RECOVER = (By.XPATH, "//*[@class= 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    BUTTON_SHOW_PASSWORD = (By.XPATH, "//*[@class='input__icon input__icon-action']")
    FIELD_PASSWORD_IS_ACTIVE = (By.XPATH, "//*[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step(f'Открыть страницу {FORGOT_PASSWORD_PAGE_URL}')
    def open(self):
        super().open(FORGOT_PASSWORD_PAGE_URL)

    @allure.step(f'Проверить, что url страницы: {FORGOT_PASSWORD_PAGE_URL}')
    def check_url_is_forgot_password_page(self):
        return self.check_url_is(FORGOT_PASSWORD_PAGE_URL)
    
    @allure.step('Заполнить поле email: {text}')
    def set_email_input(self, text):
        self.send_keys(self.INPUT_EMAIL, text)

    @allure.step('Клик на кнопку "Восстановить"')
    def click_button_recover(self):
        self.click(self.BUTTON_RECOVER)
        
    @allure.step(f'Проверить, что url страницы: {RESET_PASSWORD_PAGE_URL}')
    def check_url_is_reset_password_page(self):
        return self.check_url_is(RESET_PASSWORD_PAGE_URL)
    
    @allure.step('Клик на кнопку "Показать пароль" (иконка глаза)')
    def click_button_show_password(self):
        self.click(self.BUTTON_SHOW_PASSWORD)
    
    @allure.step('Проверить, что поле "Пароль" активно')
    def check_field_password_is_active(self):
        return self.find_element(self.FIELD_PASSWORD_IS_ACTIVE).is_displayed()
    

        
    
