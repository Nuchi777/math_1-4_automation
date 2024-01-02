import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class NumberLineAndNumberAxisLessonAcquaintedWithNumberAxisPage(BasePage):
    ZAVRIK = (By.XPATH, '//div[contains(@class,"AxisImage")]')
    BUTTON_LEFT = (By.XPATH, '//div[@data-value="-1"]')
    BUTTON_RIGHT = (By.XPATH, '//div[@data-value="+1"]')
    BUTTON_DONE = (By.XPATH, '//div[@data-value="Enter"]')
    INPUT = (By.XPATH, '//div[contains(@class, "focused")]')
    KEYBOARD = (By.XPATH, '//div[contains(@class, "KeyboardInner")]')
    BUTTON_KEY_1 = (By.XPATH, '//div[@data-value="1"]')
    BUTTON_KEY_2 = (By.XPATH, '//div[@data-value="2"]')
    BUTTON_KEY_3 = (By.XPATH, '//div[@data-value="3"]')
    BUTTON_KEY_4 = (By.XPATH, '//div[@data-value="4"]')
    BUTTON_KEY_5 = (By.XPATH, '//div[@data-value="5"]')
    BUTTON_KEY_6 = (By.XPATH, '//div[@data-value="6"]')
    BUTTON_KEY_7 = (By.XPATH, '//div[@data-value="7"]')
    BUTTON_KEY_8 = (By.XPATH, '//div[@data-value="8"]')
    BUTTON_KEY_9 = (By.XPATH, '//div[@data-value="9"]')

    def click_on_button_key_1_fill_input_1(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_1).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_2_fill_input_2(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_2).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_3_fill_input_3(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_3).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_4_fill_input_4(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_4).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_5_fill_input_5(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_5).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_6_fill_input_6(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_6).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_7_fill_input_7(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_7).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_8_fill_input_8(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_8).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_9_fill_input_9(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_9).click()
        self.element_is_invisible(self.INPUT)

    def move_zavrik_to_point_4(self):
        count = 0
        while count != 3:
            self.element_is_clickable(self.BUTTON_RIGHT).click()
            count += 1
        self.element_is_clickable(self.BUTTON_DONE).click()
        self.element_is_invisible(self.BUTTON_DONE)

    def move_zavrik_to_point_6(self):
        count = 0
        while count != 5:
            self.element_is_clickable(self.BUTTON_RIGHT).click()
            count += 1
        self.element_is_clickable(self.BUTTON_DONE).click()
        self.element_is_invisible(self.BUTTON_DONE)

    def move_zavrik_to_point_8(self):
        count = 0
        while count != 7:
            self.element_is_clickable(self.BUTTON_RIGHT).click()
            count += 1
        self.element_is_clickable(self.BUTTON_DONE).click()
        self.element_is_invisible(self.BUTTON_DONE)

    def move_zavrik_to_point_3(self):
        count = 0
        while count != 2:
            self.element_is_clickable(self.BUTTON_RIGHT).click()
            count += 1
        self.element_is_clickable(self.BUTTON_DONE).click()
        self.element_is_invisible(self.BUTTON_DONE)

    def move_zavrik_to_point_7(self):
        count = 0
        while count != 6:
            self.element_is_clickable(self.BUTTON_RIGHT).click()
            count += 1
        self.element_is_clickable(self.BUTTON_DONE).click()
        self.element_is_invisible(self.BUTTON_DONE)

    def move_zavrik_to_point_5(self):
        count = 0
        while count != 4:
            self.element_is_clickable(self.BUTTON_RIGHT).click()
            count += 1
        self.element_is_clickable(self.BUTTON_DONE).click()
        self.element_is_invisible(self.BUTTON_DONE)

    def move_zavrik_to_point_9(self):
        count = 0
        while count != 8:
            self.element_is_clickable(self.BUTTON_RIGHT).click()
            count += 1
        self.element_is_clickable(self.BUTTON_DONE).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()

