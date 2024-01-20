import time
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class IGoingToSchoolLessonDayKnowledgePage(BasePage):
    FIRST_PACKAGE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[1]')
    SECOND_PACKAGE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[2]')
    THIRD_PACKAGE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[3]')
    HOLIDAY_1_JANUARY = (By.XPATH, '(//div[contains(@class, "DraggableItemContainer")])[1]')
    HOLIDAY_9_MAY = (By.XPATH, '(//div[contains(@class, "DraggableItemContainer")])[2]')
    HOLIDAY_1_SEPTEMBER = (By.XPATH, '(//div[contains(@class, "DraggableItemContainer")])[3]')
    CARD_SITTING_DESK = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    CARD_COLLECTS_BRIEFCASE = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    BUTTON_DONE_ACTIVE = (By.XPATH, '//button[@data-component-name="button-done"]')
    BUTTON_DONE_DISABLED = (By.XPATH, '//button[contains(@class, "disabled")]')


    def drag_1_january_in_third_package(self):
        self.element_is_visible(self.HOLIDAY_1_JANUARY)
        self.drag_and_drop_on_to_element_new(self.HOLIDAY_1_JANUARY, self.THIRD_PACKAGE)
        self.element_is_invisible(self.HOLIDAY_1_JANUARY)

    def drag_9_may_in_first_package(self):
        self.element_is_visible(self.HOLIDAY_9_MAY)
        self.drag_and_drop_on_to_element_new(self.HOLIDAY_9_MAY, self.FIRST_PACKAGE)
        self.element_is_invisible(self.HOLIDAY_9_MAY)

    def drag_1_september_in_first_package(self):
        self.element_is_visible(self.HOLIDAY_1_SEPTEMBER)
        self.drag_and_drop_on_to_element_new(self.HOLIDAY_1_SEPTEMBER, self.SECOND_PACKAGE)
        self.element_is_invisible(self.HOLIDAY_1_SEPTEMBER)

    def click_on_card_sitting_at_the_desk(self):
        self.element_is_visible(self.CARD_SITTING_DESK).click()

    def click_on_card_collects_briefcase(self):
        self.element_is_visible(self.CARD_COLLECTS_BRIEFCASE).click()

    def click_on_done_button(self):
        self.element_is_invisible(self.BUTTON_DONE_DISABLED)
        self.element_is_clickable(self.BUTTON_DONE_ACTIVE).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()

