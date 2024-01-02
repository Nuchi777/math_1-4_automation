import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class FirstSecondThirdLessonWhoInWhichCarriagePage(BasePage):
    INPUT = (By.XPATH, '//div[contains(@class, "focused")]')