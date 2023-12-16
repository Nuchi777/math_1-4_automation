import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class CosmicAdventureLessonFixRocketPage(BasePage):
    BUTTON_PLAY = (By.XPATH, '//div[contains(@class, "StyledButtonWrap")]')
    BUTTON_NEXT = (By.XPATH, '//div[contains(@class, "styles__StyledNextButton-sc")]')
    BOX_THREE_STONES = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    BOX_ONE_STONES = (By.XPATH, '//div[@data-component-name="picBlockItem_4"]')
    ZAVR_FOUR_STONES = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    ZAVR_THREE_STONES = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    ELEMENT_ROCKET = (By.XPATH, '//div[contains(@class,"DraggableItemContainer")]')
    ROCKET = (By.XPATH, '//div[contains(@class,"StyledPrimarySorterMain")]')
    PROGRESS_BAR_CHUNK_2 = (By.XPATH, '//div[@width="136.78571428571428"]')
    PROGRESS_BAR_CHUNK_3 = (By.XPATH, '//div[@width="193.92857142857142"]')
    PROGRESS_BAR_CHUNK_4 = (By.XPATH, '//div[@width="251.07142857142856"]')


    def click_on_button_play(self):
        self.element_is_visible(self.BUTTON_PLAY).click()

    def click_on_box_with_three_stones(self):
        self.element_is_visible(self.BOX_THREE_STONES).click()

    def click_on_box_with_one_stone(self):
        self.element_is_visible(self.PROGRESS_BAR_CHUNK_2)
        self.element_is_visible(self.BOX_ONE_STONES).click()

    def click_on_zavrik_with_four_stones(self):
        self.element_is_visible(self.PROGRESS_BAR_CHUNK_3)
        self.element_is_visible(self.ZAVR_FOUR_STONES).click()

    def click_on_zavrik_with_three_stones(self):
        self.element_is_visible(self.PROGRESS_BAR_CHUNK_4)
        self.element_is_visible(self.ZAVR_THREE_STONES).click()

    def click_on_next_button(self):
        self.element_is_visible(self.BUTTON_NEXT).click()

    def drag_rocket_element_to_rocket(self):
        self.drag_and_drop_on_to_element_new(self.ELEMENT_ROCKET, self.ROCKET)

    def check_table_marathon_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.TABLE_MARATHON).is_displayed()


