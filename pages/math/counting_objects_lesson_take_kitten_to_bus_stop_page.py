import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class CountingObjectsLessonTakeKittenToBusStopPage(BasePage):
    BUTTON_START = (By.XPATH, '(//div[contains(@class, "styles__StyledImage-sc-1ch9bzc-0 insPLH")])[2]')