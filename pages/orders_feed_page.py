from selenium.webdriver.common.by import By
import allure

from core.urls import ORDERS_FEED_PAGE_URL
from pages.base_page import BasePage
from pages.components import HeaderComponent


class OrdersFeedPage(BasePage):
    FIRST_ORDER = (By.XPATH, "//*[@class='OrderHistory_listItem__2x95r mb-6'][1]")
    MODAL_WINDOW_INFO_ORDER = (By.XPATH, "//*[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    ID_ORDER = (By.XPATH, "//*[@class='text text_type_digits-default']")
    COUNTER_COMPLETED_ALL_TIME = (By.XPATH, "(//*[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")
    COUNTER_COMPLETED_TODAY = (By.XPATH, "(//*[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver)

    @allure.step(f'Открыть страницу {ORDERS_FEED_PAGE_URL}')
    def open(self):
        super().open(ORDERS_FEED_PAGE_URL)

    @allure.step(f'Проверить, что url страницы: {ORDERS_FEED_PAGE_URL}')
    def check_url_is_orders_feed_page(self):
        return self.check_url_is(ORDERS_FEED_PAGE_URL)
    
    @allure.step('Клик на первый заказ')
    def click_first_order(self):
        self.click(self.FIRST_ORDER)

    @allure.step('Проверить, что модальное окно с информацией о заказе отображается')
    def check_modal_window_info_order_is_displayed(self):
        return self.find_element(self.MODAL_WINDOW_INFO_ORDER).is_displayed()
    
    @allure.step('Получить список заказов из "Ленты заказов"')
    def get_list_orders_feed(self):
        elements = self.find_elements(self.ID_ORDER)
        ids_orders_in_orders_feed = []
        for element in elements:
            ids_orders_in_orders_feed.append(element.text)

        return ids_orders_in_orders_feed
    
    @allure.step('Проверить, что заказы есть в "Ленте заказов"')
    def check_orders_in_orders_feed(self, ids_orders, ids_orders_in_orders_feed):
        for id in ids_orders:
            if id not in ids_orders_in_orders_feed:
                return False
        return True

    @allure.step('Получить количество заказов за все время')
    def get_counter_completed_all_time(self):
        return self.text(self.COUNTER_COMPLETED_ALL_TIME)

    @allure.step('Получить количество заказов за сегодня')
    def get_counter_completed_today(self):
        return self.text(self.COUNTER_COMPLETED_TODAY)
    
    @allure.step('Получить список заказов "В работе"')
    def get_list_orders_in_progress(self):
        elements = self.find_elements(self.ID_ORDER)
        ids_orders_in_progress = []
        for element in elements:
            ids_orders_in_progress.append(element.text)

        return ids_orders_in_progress