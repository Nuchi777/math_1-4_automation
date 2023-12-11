from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class CosmicAdventureLessonStartPage(BasePage):

    BUTTON_START = (By.XPATH, '(//div[contains(@class, "styles__StyledImage-sc-1ch9bzc-0 insPLH")])[2]')
    BUTTON_NEXT = (By.XPATH, '//div[contains(@class, "styles__StyledNextButton-sc")]')
    KEYBOARD = (By.XPATH, '//div[contains(@class, "StyledKeyboardInner")]')
    INPUT_1 = (By.XPATH, '(//div[contains(@class, "styles__StyledPrimaryInputInner-sc")])[1]')
    INPUT_2 = (By.XPATH, '(//div[contains(@class, "styles__StyledPrimaryInputInner-sc")])[2]')
    INPUT_3 = (By.XPATH, '(//div[contains(@class, "styles__StyledPrimaryInputInner-sc")])[3]')
    INPUT_4 = (By.XPATH, '(//div[contains(@class, "styles__StyledPrimaryInputInner-sc")])[4]')
    INPUT_5 = (By.XPATH, '(//div[contains(@class, "styles__StyledPrimaryInputInner-sc")])[5]')
    BUTTON_KEY_3 = (By.XPATH, '//div[contains(@class, "styles__StyledKey-sc")][text()="3"]')
    BUTTON_KEY_4 = (By.XPATH, '//div[contains(@class, "styles__StyledKey-sc")][text()="4"]')
    BUTTON_KEY_5 = (By.XPATH, '//div[contains(@class, "styles__StyledKey-sc")][text()="5"]')

    def click_on_button_start(self):
        self.element_is_visible(self.BUTTON_START).click()

    def click_on_button_key_3_fill_input_1(self):
        self.element_is_visible(self.INPUT_1)
        self.element_is_visible(self.BUTTON_KEY_3).click()

    def click_on_button_key_4_fill_input_2(self):
        self.element_is_visible(self.INPUT_2)
        self.element_is_visible(self.BUTTON_KEY_4).click()

    def click_on_button_key_5_fill_input_3(self):
        self.element_is_visible(self.INPUT_3)
        self.element_is_visible(self.BUTTON_KEY_5).click()

    def click_on_button_key_5_fill_input_4(self):
        self.element_is_visible(self.INPUT_4)
        self.element_is_visible(self.BUTTON_KEY_5).click()

    def click_on_button_key_5_fill_input_5(self):
        self.element_is_visible(self.INPUT_5)
        self.element_is_visible(self.BUTTON_KEY_3).click()

    def click_on_next_button(self):
        self.element_is_visible(self.BUTTON_NEXT).click()
