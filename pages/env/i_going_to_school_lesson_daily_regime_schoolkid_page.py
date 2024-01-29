import time
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class IGoingToSchoolLessonDailyRegimeSchoolkidPage(BasePage):
    CARD_2_STATE_ACTIVE = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    CARD_2_STATE_DONE = (By.XPATH, '//div[@data-component-name="picBlockItem_1"][contains(@class, "state_done")]')
    CARD_3_STATE_ACTIVE = (By.XPATH, '//div[@data-component-name="picBlockItem_2"]')
    CARD_3_STATE_DONE = (By.XPATH, '//div[@data-component-name="picBlockItem_2"][contains(@class, "state_done")]')
    CARD_4_STATE_ACTIVE = (By.XPATH, '//div[@data-component-name="picBlockItem_3"]')
    CARD_4_STATE_DONE = (By.XPATH, '//div[@data-component-name="picBlockItem_3"][contains(@class, "state_done")]')
    CARD_5_STATE_ACTIVE = (By.XPATH, '//div[@data-component-name="picBlockItem_4"]')
    CARD_5_STATE_DONE = (By.XPATH, '//div[@data-component-name="picBlockItem_4"][contains(@class, "state_done")]')
    CARD_6_STATE_ACTIVE = (By.XPATH, '//div[@data-component-name="picBlockItem_5"]')
    CARD_6_STATE_DONE = (By.XPATH, '//div[@data-component-name="picBlockItem_5"][contains(@class, "state_done")]')
    SHUFFLE_CARD_1 = (By.XPATH, '(//div[@data-component-name="shuffle-drag-item"])[1]')
    SHUFFLE_CARD_2 = (By.XPATH, '(//div[@data-component-name="shuffle-drag-item"])[2]')


    def click_on_card_with_time_8_00(self):
        self.element_is_visible(self.CARD_2_STATE_ACTIVE).click()
        self.element_is_presence(self.CARD_2_STATE_DONE)

    def click_on_card_with_time_8_30(self):
        self.element_is_visible(self.CARD_3_STATE_ACTIVE).click()
        self.element_is_presence(self.CARD_3_STATE_DONE)

    def click_on_card_with_time_13_00(self):
        self.element_is_visible(self.CARD_4_STATE_ACTIVE).click()
        self.element_is_presence(self.CARD_4_STATE_DONE)

    def click_on_card_with_time_17_00(self):
        self.element_is_visible(self.CARD_5_STATE_ACTIVE).click()
        self.element_is_presence(self.CARD_5_STATE_DONE)

    def click_on_card_with_time_21_00(self):
        self.element_is_visible(self.CARD_6_STATE_ACTIVE).click()
        self.element_is_presence(self.CARD_6_STATE_DONE)

    def drag_card_wake_up_for_time_7_30(self):
        self.drag_and_drop_on_to_element(self.SHUFFLE_CARD_2, self.SHUFFLE_CARD_1)

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()
