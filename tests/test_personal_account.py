import allure

from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestRecoverPassword:

    @allure.title('Переход на страницу "Личный кабинет" авторизованным пользователем по клику на "Личный кабинет"')
    def test_click_personal_account_auth_user_open_personal_account_page(self, driver, login_new_user):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        main_page.header.click_button_personal_account()

        assert personal_account_page.check_url_is_personal_account_page() 

    @allure.title('Переход на страницу "Авторизация" неавторизованным пользователем по клику на "Личный кабинет"')
    def test_click_personal_account_unauth_user_open_login_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open()
        main_page.header.click_button_personal_account()

        assert login_page.check_url_is_login_page() 


    @allure.title('Переход на страницу "История заказов" по клику на "История заказов"')
    def test_click_orders_history_open_orders_history_page(self, driver, login_new_user):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        main_page.header.click_button_personal_account()
        personal_account_page.click_orders_history()

        assert personal_account_page.check_url_is_orders_history_page() 

    
    @allure.title('Выход из аккаунта по клику на "Выход"')
    def test_click_button_logout_open_login_page(self, driver, login_new_user):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        login_page = LoginPage(driver)
        main_page.header.click_button_personal_account()
        personal_account_page.click_button_logout()

        assert login_page.check_url_is_login_page()