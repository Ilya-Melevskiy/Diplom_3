import allure

from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrdersFeed:

    @allure.title('По клику на заказ, открывается всплывающее окно заказа')
    def test_click_order_open_modal_window_info_order(self, driver, create_order):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open()
        orders_feed_page.click_first_order()

        assert orders_feed_page.check_modal_window_info_order_is_displayed()


    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_create_order_orders_in_history_is_displayed_in_orders_feed(self, driver, create_order):
        personal_account_page = PersonalAccountPage(driver)
        orders_feed_page = OrdersFeedPage(driver)
        main_page = MainPage(driver)
        main_page.open()
        main_page.header.click_button_personal_account()
        personal_account_page.click_orders_history()
        ids_orders = personal_account_page.get_list_orders_history()
        orders_feed_page.open()
        ids_orders_in_feed = orders_feed_page.get_list_orders_feed()
        
        assert orders_feed_page.check_orders_in_orders_feed(ids_orders, ids_orders_in_feed)


    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_create_order_counter_completed_all_time_increases(self, driver, request):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open()
        counter_completed_all_time_before_create_order = orders_feed_page.get_counter_completed_all_time()
        request.getfixturevalue("create_order")
        orders_feed_page.open()
        counter_completed_all_time_after_create_order = orders_feed_page.get_counter_completed_all_time()

        assert counter_completed_all_time_after_create_order > counter_completed_all_time_before_create_order
        

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_create_order_counter_completed_today_increases(self, driver, request):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open()
        counter_completed_today_before_create_order = orders_feed_page.get_counter_completed_today()
        request.getfixturevalue("create_order")
        orders_feed_page.open()
        counter_completed_today_after_create_order = orders_feed_page.get_counter_completed_today()

        assert counter_completed_today_after_create_order > counter_completed_today_before_create_order

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_create_order_order_is_displayed_in_progress(self, driver, create_order):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open()
        ids_orders_in_progress = orders_feed_page.get_list_orders_in_progress()
        
        assert f'#0{create_order}' in ids_orders_in_progress