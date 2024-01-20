import time
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class IGoingToSchoolLessonGetReadyForSchoolPage(BasePage):
    BAG_TAKE_TO_SCHOOL = (By.XPATH, '(//div[contains(@class, "DropContainer")])[1]')
    BAG_LEAVE_AT_HOME = (By.XPATH, '(//div[contains(@class, "DropContainer")])[2]')
    ITEMS = (By.XPATH, '//div[contains(@class, "DraggableItemContainer")]')
    ICE_CREAM_STATE_ACTIVE = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    ICE_CREAM_STATE_DONE = (By.XPATH, '//div[@data-component-name="picBlockItem_1"][contains(@class, "state_done")]')
    CAT_STATE_ACTIVE = (By.XPATH, '//div[@data-component-name="picBlockItem_7"]')
    CAT_STATE_DONE = (By.XPATH, '//div[@data-component-name="picBlockItem_7"][contains(@class, "state_done")]')
    SLED_STATE_ACTIVE = (By.XPATH, '//div[@data-component-name="picBlockItem_6"]')
    SLED_STATE_DONE = (By.XPATH, '//div[@data-component-name="picBlockItem_6"][contains(@class, "state_done")]')


    def drag_kite_in_leave_at_home_bag(self):
        self.drag_and_drop_on_to_element_new(self.ITEMS, self.BAG_LEAVE_AT_HOME)

    def drag_book_in_take_to_school_bag(self):
        self.drag_and_drop_on_to_element_new(self.ITEMS, self.BAG_TAKE_TO_SCHOOL)

    def drag_pencil_case_in_take_to_school_bag(self):
        self.drag_and_drop_on_to_element_new(self.ITEMS, self.BAG_TAKE_TO_SCHOOL)

    def drag_ice_cream_in_leave_at_home_bag(self):
        self.drag_and_drop_on_to_element_new(self.ITEMS, self.BAG_LEAVE_AT_HOME)

    def drag_notebook_in_take_to_school_bag(self):
        self.drag_and_drop_on_to_element_new(self.ITEMS, self.BAG_TAKE_TO_SCHOOL)

    def click_on_ice_cream(self):
        self.element_is_visible(self.ICE_CREAM_STATE_ACTIVE).click()
        self.element_is_presence(self.ICE_CREAM_STATE_DONE)

    def click_on_sled(self):
        self.element_is_visible(self.SLED_STATE_ACTIVE).click()
        self.element_is_presence(self.SLED_STATE_DONE)

    def click_on_cat(self):
        self.element_is_visible(self.CAT_STATE_ACTIVE).click()
        self.element_is_presence(self.CAT_STATE_DONE)

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()
