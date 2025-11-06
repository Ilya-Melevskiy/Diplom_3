import pytest
import requests

from core.browser_factory import BrowserFactory
from pages.main_page import MainPage
from core.helpers import Helpers
from core.urls import CREATE_USER, DEL_USER, LOGIN_USER


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = BrowserFactory.get_driver(request.param, headless=False)
    yield driver
    driver.quit()


@pytest.fixture
def login_new_user(driver):
    email = f'{Helpers.generate_random_string(10)}@mail.ru'
    password = Helpers.generate_random_string(10)
    name = Helpers.generate_random_string(10)
    payload = {'email': email,
                'password': password,
                'name': name}
    
    response = requests.post(CREATE_USER, json=payload)

    if response.status_code == 200:
        login_pass = payload

    payload_login = {'email': email,
                'password': password
                }
    response_login = requests.post(LOGIN_USER, json=payload_login)

    access_token = response_login.json()['accessToken']
    refresh_token = response_login.json()['refreshToken']
    main_page = MainPage(driver)
    main_page.open()
    driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", 'accessToken',
                          access_token)
    driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);",
                          'refreshToken', refresh_token)

    yield {'response': response, 'login_pass': login_pass}

    requests.delete(DEL_USER, json=payload, headers={'Authorization': access_token})


@pytest.fixture
def create_order(driver, login_new_user):
    main_page = MainPage(driver)
    main_page.open()
    main_page.drag_and_drop_first_bun_in_order()
    main_page.click_button_create_order()
    id_order = main_page.get_id_order()
    
    return id_order

