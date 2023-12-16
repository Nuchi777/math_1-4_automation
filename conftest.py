import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import data
from locators.main_page_locators import MainPageLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(data.Urls.URL_MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
    driver.find_element(*MainPageLocators.LOGIN_FIELD).send_keys(data.UserData.USER_LOGIN)
    driver.find_element(*MainPageLocators.PASSWORD_FIELD).send_keys(data.UserData.USER_PASSWORD)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(MainPageLocators.HEADBAR_LOGO))
    return driver

