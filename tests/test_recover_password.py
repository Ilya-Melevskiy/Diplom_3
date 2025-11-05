import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


class TestRecoverPassword:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_button_recover_password_open_recover_password_page(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        login_page.open()
        login_page.click_button_recover_password()

        assert forgot_password_page.check_url_is_forgot_password_page()


    @allure.title('Ввод почты и клик на кнопку "Восстановить" открывают страницу для ввода нового пароля')
    def test_set_email_input_click_button_recover_open_reset_password_page(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        forgot_password_page.set_email_input('test@mail.ru')
        forgot_password_page.click_button_recover()

        assert forgot_password_page.check_url_is_reset_password_page()


    @allure.title('Клик по кнопке показать/скрыть пароль делает поле "Пароль" активным')
    def test_click_button_show_password_makes_field_password_is_active(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        forgot_password_page.set_email_input('test@mail.ru')
        forgot_password_page.click_button_recover()
        forgot_password_page.click_button_show_password()
        assert forgot_password_page.check_field_password_is_active()
        