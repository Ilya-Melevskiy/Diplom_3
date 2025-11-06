from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    OVERLAY = (By.XPATH, "//section[@class ='Modal_modal__P3_V5']/*[@class = 'Modal_modal_overlay__x2ZCr']")
    OVERLAY_2 = (By.XPATH, "//div[@class ='Modal_modal__P3_V5']/*[@class = 'Modal_modal_overlay__x2ZCr']")
    

    def __init__(self, driver): 
        self.driver = driver 

    def wait_visibility(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def wait_invisibility(self, locator):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))

    def wait_overlay_invisibility(self):
        self.wait_invisibility(self.OVERLAY)
        self.wait_invisibility(self.OVERLAY_2)
    
    def wait_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    def wait_url(self, url):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(url))

    def wait_text_locator_is_not_equal_text(self, locator, text):
        WebDriverWait(self.driver, 5).until(lambda driver: self.text(locator) != text)

    def find_element(self, locator): 
        self.wait_visibility(locator)
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator): 
        self.wait_visibility(locator)
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait_overlay_invisibility()
        self.wait_clickable(locator)
        self.find_element(locator).click()

    def text(self, locator):
        self.wait_overlay_invisibility()
        self.wait_visibility(locator)
        return self.find_element(locator).text
    
    def send_keys(self, locator, text):
        self.wait_visibility(locator)
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)
        
    def open(self, url):
        self.driver.get(url)
        self.wait_overlay_invisibility()

    def switch_to_window(self, number):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[number])

    def scroll_to_element(self, locator):
        self.wait_visibility(locator)
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def check_url_is(self, url):
        try:
            self.wait_url(url)
        except Exception:
            return False
        return self.driver.current_url == url
    
    def drag_and_drop(self, locator_1, locator_2):
        # Реализовал через js, потому что через ActionChains drag and drop не работает в firefox
        js_code = """
        const dataTransfer = new DataTransfer();
        ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend'].forEach(eventType => {
            const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
            (eventType === 'dragstart' || eventType === 'dragend' ? arguments[0] : arguments[1]).dispatchEvent(event);
        });
        """
        self.driver.execute_script(js_code, self.find_element(locator_1), self.find_element(locator_2))