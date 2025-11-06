from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import allure

from core.urls import MAIN_PAGE_URL
from pages.base_page import BasePage
from pages.components import HeaderComponent


class MainPage(BasePage):

    FIRST_BUN = (By.XPATH, "(//*[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'])[1]")
    MODAL_WINDOW_INGREDIENT = (By.XPATH, "//*[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']")
    CROSS_IN_MODAL_WINDOW_INGREDIENT = (By.XPATH, "(//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'])[1]")
    FIRST_SAUCE = (By.XPATH, "//*[@class='BurgerIngredients_ingredients__list__2A-mT'][2]/*[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'][1]")
    COUNTER_FIRST_SAUCE = (By.XPATH, "//*[@class='BurgerIngredients_ingredients__list__2A-mT'][2]/"
    "*[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'][1]//*[@class='counter_counter__num__3nue1']")
    ORDER_INGREDIENTS_LIST = (By.XPATH, "//*[@class='constructor-element__price']")
    BUTTON_CREATE_ORDER = (By.XPATH, "//*[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    MODAL_WINDOW_ORDER_IS_CREATED = (By.XPATH, "//*[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']")
    ID_ORDER = (By.XPATH, "//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver)

    @allure.step(f'Открыть страницу {MAIN_PAGE_URL}')
    def open(self):
        super().open(MAIN_PAGE_URL)

    @allure.step(f'Проверить, что url страницы: {MAIN_PAGE_URL}')
    def check_url_is_main_page(self):
        return self.check_url_is(MAIN_PAGE_URL)
    
    @allure.step('Клик на первый ингредиент')
    def click_first_ingredient(self):
        self.click(self.FIRST_BUN)

    @allure.step('Проверить, что модальное окно ингредиента отображается')
    def check_modal_window_ingredient_is_displayed(self):
        return self.find_element(self.MODAL_WINDOW_INGREDIENT).is_displayed()
    
    @allure.step('Клик на крестик в модальном окне ингредиента')
    def click_cross_in_modal_window_ingredient(self):
        self.click(self.CROSS_IN_MODAL_WINDOW_INGREDIENT)

    @allure.step('Проверить, что модальное окно ингредиента не отображается')
    def check_modal_window_ingredient_is_not_displayed(self):
        try:
            element = self.find_element(self.MODAL_WINDOW_INGREDIENT)
            self.wait_invisibility(self.MODAL_WINDOW_INGREDIENT)
            return not element.is_displayed()
        except NoSuchElementException:
            return True
    
    @allure.step('Перетащить первый соус в заказ')
    def drag_and_drop_first_sauce_in_order(self):
        self.drag_and_drop(self.FIRST_SAUCE, self.ORDER_INGREDIENTS_LIST)
    
    @allure.step('Перетащить первую булку в заказ')
    def drag_and_drop_first_bun_in_order(self):
        self.drag_and_drop(self.FIRST_BUN, self.ORDER_INGREDIENTS_LIST)

    @allure.step('Проверить, что значение в счетчике: "1"')
    def check_counter_is_one(self):
        return self.text(self.COUNTER_FIRST_SAUCE) == '1'
    
    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_button_create_order(self):
        self.click(self.BUTTON_CREATE_ORDER)

    @allure.step('Проверить, что модальное окно "Заказ создан" отображается')
    def check_modal_window_order_is_created_is_displayed(self):
        return self.find_element(self.MODAL_WINDOW_ORDER_IS_CREATED).is_displayed()
    
    @allure.step('Получить id заказа из окна "Заказ создан"')
    def get_id_order(self):
        WebDriverWait(self.driver, 5).until(lambda driver: self.text(self.ID_ORDER) != '9999')
        return self.text(self.ID_ORDER)
    

    