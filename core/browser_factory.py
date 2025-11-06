from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


class BrowserFactory:

    @staticmethod
    def get_driver(browser_name: str, headless: bool = False): 
        if browser_name.lower() == 'chrome':
            options = ChromeOptions()
            options.add_argument('--window-size=1920,1080')
            if headless:
                options.add_argument('--headless')
            return webdriver.Chrome(options=options) 
        elif browser_name.lower() == 'firefox':
            options = FirefoxOptions()
            options.add_argument('--width=1920')
            options.add_argument('--height=1080')
            if headless:
                options.add_argument('--headless')
            return webdriver. Firefox (options=options)
        else:
            raise ValueError(f'Browser {browser_name} is not supported.')