import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
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
    BUTTON_KEY_3 = (By.XPATH, '//div[@data-value="3"]')
    BUTTON_KEY_4 = (By.XPATH, '//div[@data-value="4"]')
    BUTTON_KEY_5 = (By.XPATH, '//div[@data-value="5"]')
    BUTTON_6_3_8 = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    BUTTON_1_5_4 = (By.XPATH, '//div[@data-component-name="picBlockItem_2"]')
    POINT_ABOVE_STONE = (By.XPATH, '//div[@class="styles__StyledPicBlockContent-sc-1j9mray-1 dQTgGg choiceImage state_active"]')
    POINT_BELOW_STONE = (By.XPATH, '//div[@class="styles__StyledPicBlockContent-sc-1j9mray-1 kxuuiu choiceImage state_active"]')
    POINT_BETWEEN_STONE = (By.XPATH, '(//div[contains(@class, "styles__StyledPicBlockContent-sc")])[11]')
    POINT_BELOW_TRIANG_AND_ABOVE_ROUND_STONE = (By.XPATH, '(//div[contains(@class, "styles__StyledPicBlockContent-sc")])[21]')
    PORTHOLE = (By.XPATH, '//div[@id="containerScene"]')
    BUTTON_2_STEP_1 = (By.XPATH, '(//div[contains(@class, "WIkZv active")])[2]')
    BUTTON_3_STEP_1 = (By.XPATH, '(//div[contains(@class, "WIkZv active")])[1]')
    BUTTON_4_STEP_1 = (By.XPATH, '(//div[contains(@class, "WIkZv active")])[3]')
    BUTTON_5_STEP_1 = (By.XPATH, '(//div[contains(@class, "WIkZv active")])[2]')
    BUTTON_6_STEP_1 = (By.XPATH, '(//div[contains(@class, "WIkZv active")])[2]')
    BUTTON_2_STEP_2 = (By.XPATH, '(//div[contains(@class, "WIkZv active")])[2]')
    BUTTON_4_STEP_2 = (By.XPATH, '(//div[contains(@class, "WIkZv active")])[1]')
    BUTTON_6_STEP_2 = (By.XPATH, '(//div[contains(@class, "WIkZv active")])[1]')
    BUTTON_8_STEP_2 = (By.XPATH, '(//div[contains(@class, "WIkZv active")])[3]')
    BUTTON_10_STEP_2 = (By.XPATH, '(//div[contains(@class, "WIkZv active")])[2]')
    PROGRESS_BAR_BUTTON_1_5_4 = (By.XPATH, '//div[@width="140.14705882352942"]')
    PROGRESS_BAR_PORTHOLE_1 = (By.XPATH, '//div[@width="304.8529411764706"]')
    PROGRESS_BAR_PORTHOLE_2 = (By.XPATH, '//div[@width="328.38235294117646"]')

    def click_on_button_start(self):
        self.element_is_visible(self.BUTTON_START).click()

    def click_on_next_button(self):
        self.element_is_visible(self.BUTTON_NEXT).click()

    def click_on_button_key_3_fill_input_1(self):
        self.element_is_clickable(self.INPUT_1)
        self.element_is_visible(self.BUTTON_KEY_3).click()

    def click_on_button_key_4_fill_input_2(self):
        self.element_is_clickable(self.INPUT_2)
        self.element_is_visible(self.BUTTON_KEY_4).click()

    def click_on_button_key_5_fill_input_3(self):
        self.element_is_clickable(self.INPUT_3)
        self.element_is_visible(self.BUTTON_KEY_5).click()

    def click_on_button_key_5_fill_input_4(self):
        self.element_is_clickable(self.INPUT_4)
        self.element_is_visible(self.BUTTON_KEY_5).click()

    def click_on_button_key_5_fill_input_5(self):
        self.element_is_clickable(self.INPUT_5)
        self.element_is_visible(self.BUTTON_KEY_3).click()

    def click_on_button_6_3_8(self):
        self.element_is_clickable(self.BUTTON_6_3_8).click()

    def click_on_button_1_5_4(self):
        self.element_is_visible(self.PROGRESS_BAR_BUTTON_1_5_4)
        self.element_is_clickable(self.BUTTON_1_5_4).click()

    def click_on_point_above_stone(self):
        self.element_is_visible(self.POINT_ABOVE_STONE).click()

    def click_on_point_below_stone(self):
        self.element_is_visible(self.POINT_BELOW_STONE).click()

    def click_on_point_between_stone(self):
        self.element_is_visible(self.POINT_BETWEEN_STONE).click()

    def click_on_point_below_triangular_and_above_round_stone(self):
        self.element_is_visible(self.POINT_BELOW_TRIANG_AND_ABOVE_ROUND_STONE).click()

    def click_on_first_porthole_3_times(self):
        self.element_is_visible(self.PROGRESS_BAR_PORTHOLE_1)
        time.sleep(1)
        self.element_is_visible(self.PORTHOLE).click()
        self.element_is_visible(self.PORTHOLE).click()
        self.element_is_visible(self.PORTHOLE).click()

    def click_on_second_porthole_3_times(self):
        self.element_is_visible(self.PROGRESS_BAR_PORTHOLE_2)
        self.element_is_visible(self.PORTHOLE).click()
        self.element_is_visible(self.PORTHOLE).click()
        self.element_is_visible(self.PORTHOLE).click()

    def click_on_button_with_number_2_step_1(self):
        self.element_is_visible(self.BUTTON_2_STEP_1).click()

    def click_on_button_with_number_3_step_1(self):
        self.element_is_visible(self.BUTTON_3_STEP_1).click()

    def click_on_button_with_number_4_step_1(self):
        self.element_is_visible(self.BUTTON_4_STEP_1).click()

    def click_on_button_with_number_5_step_1(self):
        self.element_is_visible(self.BUTTON_5_STEP_1).click()

    def click_on_button_with_number_6_step_1(self):
        self.element_is_visible(self.BUTTON_6_STEP_1).click()

    def click_on_button_with_number_2_step_2(self):
        self.element_is_visible(self.BUTTON_2_STEP_2).click()

    def click_on_button_with_number_4_step_2(self):
        self.element_is_visible(self.BUTTON_4_STEP_2).click()

    def click_on_button_with_number_6_step_2(self):
        self.element_is_visible(self.BUTTON_6_STEP_2).click()

    def click_on_button_with_number_8_step_2(self):
        self.element_is_visible(self.BUTTON_8_STEP_2).click()

    def click_on_button_with_number_10_step_2(self):
        self.element_is_visible(self.BUTTON_10_STEP_2).click()

    def check_table_marathon_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.TABLE_MARATHON).is_displayed()
