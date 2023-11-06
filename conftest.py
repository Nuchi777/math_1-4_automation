import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import data
from locators.login_page_locators import LoginPageLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(data.Urls.URL_MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    WebDriverWait(driver, timeout=5).until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
    driver.find_element(*LoginPageLocators.LOGIN_FIELD).send_keys(data.LoginUser.USER_LOGIN)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(data.LoginUser.USER_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    return driver
