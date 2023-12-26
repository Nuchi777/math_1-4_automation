from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class CountingObjectsLessonWhichBusStopKittenPage(BasePage):
    INPUT = (By.XPATH, '//div[contains(@class, "focused")]')
    BUTTON_KEY_4 = (By.XPATH, '//div[@data-value="4"]')
    BUTTON_KEY_3 = (By.XPATH, '//div[@data-value="3"]')
    BUTTON_KEY_6 = (By.XPATH, '//div[@data-value="6"]')
    BUTTON_KEY_1 = (By.XPATH, '//div[@data-value="1"]')
    BUTTON_KEY_7 = (By.XPATH, '//div[@data-value="7"]')
    BUTTON_KEY_5 = (By.XPATH, '//div[@data-value="5"]')


    def click_on_button_key_4_fill_input_1(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_4).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_3_fill_input_2(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_3).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_6_fill_input_3(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_6).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_1_fill_input_4(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_1).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_7_fill_input_5(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_7).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_5_fill_input_6(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_5).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()