import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage


class TestBasicFunc:

    @allure.title('Переход на главную по клику на "Конструктор"')
    def test_click_button_constructor_open_main_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        login_page.open()
        login_page.header.click_button_constructor()

        assert main_page.check_url_is_main_page() 
    

    @allure.title('Переход на ленту заказов по клику на "Лента заказов"')
    def test_click_button_orders_feed_open_orders_feed_page(self, driver):
        main_page = MainPage(driver)
        orders_feed_page = OrdersFeedPage(driver)
        main_page.open()
        main_page.header.click_button_orders_feed()

        assert orders_feed_page.check_url_is_orders_feed_page() 


    @allure.title('По клику на ингредиент появляется всплывающее окно ингредиента с деталями')
    def test_click_ingredient_open_modal_window_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_first_ingredient()

        assert main_page.check_modal_window_ingredient_is_displayed()


    @allure.title('Всплывающее окно ингредиента закрывается по клику на крестик')
    def test_click_cross_in_modal_window_ingredient_close_modal_window_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_first_ingredient()
        main_page.click_cross_in_modal_window_ingredient()

        assert main_page.check_modal_window_ingredient_is_not_displayed()


    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_in_order_counter_number_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_and_drop_first_sauce_in_order()

        assert main_page.check_counter_is_one()

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_click_button_create_order_auth_user_modal_window_order_is_created_is_displayed(self, driver, login_new_user):
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_and_drop_first_bun_in_order()
        main_page.click_button_create_order()
        assert main_page.check_modal_window_order_is_created_is_displayed()


