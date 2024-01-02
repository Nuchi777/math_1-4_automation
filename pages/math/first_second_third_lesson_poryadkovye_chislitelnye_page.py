import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class FirstSecondThirdLessonPoryadkovyeChislitelnyePage(BasePage):
    INPUT = (By.XPATH, '//div[contains(@class, "focused")]')
    BUTTON_KEY_5 = (By.XPATH, '//div[@data-value="5"]')
    FIRST_ZAVR = (By.XPATH, '//*[@id="Vector_33-822"]')
    THIRD_ZAVR = (By.XPATH, '//*[@id="Vector_10-521"]')

    def click_on_button_key_5_fill_input(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_5).click()

    def drag_first_zavrik_on_first_position(self):
        self.drag_and_drop_on_to_element(self.FIRST_ZAVR, self.THIRD_ZAVR)