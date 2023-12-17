import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class CosmicAdventureLessonStartPage(BasePage):
    BUTTON_START = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    BUTTON_NEXT = (By.XPATH, '//div[contains(@class, "NextButton")]')
    INPUT = (By.XPATH, '//div[contains(@class, "focused")]')
    BUTTON_KEY_3 = (By.XPATH, '//div[@data-value="3"]')
    BUTTON_KEY_4 = (By.XPATH, '//div[@data-value="4"]')
    BUTTON_KEY_5 = (By.XPATH, '//div[@data-value="5"]')
    BUTTON_6_3_8 = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    BUTTON_1_5_4 = (By.XPATH, '//div[@data-component-name="picBlockItem_2"]')
    POINT_ABOVE_STONE = (By.XPATH, '//div[@data-component-name="picBlockItem_3"]')
    POINT_BELOW_STONE = (By.XPATH, '//div[@data-component-name="picBlockItem_17"]')
    POINT_BETWEEN_STONE = (By.XPATH, '//div[@data-component-name="picBlockItem_10"]')
    POINT_BELOW_TRIANG_AND_ABOVE_ROUND_STONE = (By.XPATH, '//div[@data-component-name="picBlockItem_20"]')
    PORTHOLE = (By.XPATH, '//div[@id="containerScene"]')
    BUTTON_2 = (By.XPATH, '//div[@data-maze-cell-value="2"]')
    BUTTON_3 = (By.XPATH, '//div[@data-maze-cell-value="3"]')
    BUTTON_4 = (By.XPATH, '//div[@data-maze-cell-value="4"]')
    BUTTON_5 = (By.XPATH, '//div[@data-maze-cell-value="5"]')
    BUTTON_6 = (By.XPATH, '//div[@data-maze-cell-value="6"]')
    BUTTON_8 = (By.XPATH, '//div[@data-maze-cell-value="8"]')
    BUTTON_10 = (By.XPATH, '//div[@data-maze-cell-value="10"]')
    PROGRESS_BAR_PORTHOLE_1 = (By.XPATH, '//div[@width="304.8529411764706"]')
    PROGRESS_BAR_PORTHOLE_2 = (By.XPATH, '//div[@width="328.38235294117646"]')

    def click_on_button_start(self):
        self.element_is_visible(self.BUTTON_START).click()

    def click_on_next_button(self):
        self.element_is_visible(self.BUTTON_NEXT).click()

    def click_on_button_key_3_fill_input_1(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_3).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_4_fill_input_2(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_4).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_5_fill_input_3(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_5).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_5_fill_input_4(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_5).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_5_fill_input_5(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_3).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_6_3_8(self):
        self.element_is_visible(self.BUTTON_6_3_8).click()
        self.element_is_invisible(self.BUTTON_6_3_8)

    def click_on_button_1_5_4(self):
        self.element_is_visible(self.BUTTON_1_5_4).click()
        self.element_is_invisible(self.BUTTON_1_5_4)

    def click_on_point_above_stone(self):
        self.element_is_visible(self.POINT_ABOVE_STONE).click()
        self.element_is_invisible(self.POINT_ABOVE_STONE)

    def click_on_point_below_stone(self):
        self.element_is_visible(self.POINT_BELOW_STONE).click()
        self.element_is_invisible(self.POINT_BELOW_STONE)

    def click_on_point_between_stone(self):
        self.element_is_visible(self.POINT_BETWEEN_STONE).click()
        self.element_is_invisible(self.POINT_BETWEEN_STONE)

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
        time.sleep(1)
        self.element_is_visible(self.PORTHOLE).click()
        self.element_is_visible(self.PORTHOLE).click()
        self.element_is_visible(self.PORTHOLE).click()

    def click_on_button_with_number_2_step_1(self):
        self.element_is_visible(self.BUTTON_2).click()

    def click_on_button_with_number_3_step_1(self):
        self.element_is_visible(self.BUTTON_3).click()

    def click_on_button_with_number_4_step_1(self):
        self.element_is_visible(self.BUTTON_4).click()

    def click_on_button_with_number_5_step_1(self):
        self.element_is_visible(self.BUTTON_5).click()

    def click_on_button_with_number_6_step_1(self):
        self.element_is_visible(self.BUTTON_6).click()

    def click_on_button_with_number_2_step_2(self):
        self.element_is_visible(self.BUTTON_2).click()

    def click_on_button_with_number_4_step_2(self):
        self.element_is_visible(self.BUTTON_4).click()

    def click_on_button_with_number_6_step_2(self):
        self.element_is_visible(self.BUTTON_6).click()

    def click_on_button_with_number_8_step_2(self):
        self.element_is_visible(self.BUTTON_8).click()

    def click_on_button_with_number_10_step_2(self):
        self.element_is_visible(self.BUTTON_10).click()

    def check_table_marathon_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.TABLE_MARATHON).is_displayed()
