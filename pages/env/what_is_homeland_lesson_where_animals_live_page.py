from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class WhatIsHomelandLessonWhereAnimalsLivePage(BasePage):
    FIRST_PACKAGE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[1]')
    SECOND_PACKAGE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[2]')
    THIRD_PACKAGE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[3]')
    CARD_FISH = (By.XPATH, '(//div[contains(@class, "DraggableItemContainer")])[1]')
    CARD_MONKEY = (By.XPATH, '(//div[contains(@class, "DraggableItemContainer")])[2]')
    CARD_BIRD = (By.XPATH, '(//div[contains(@class, "DraggableItemContainer")])[3]')

    def drag_card_fish_in_package_in_river(self):
        self.element_is_visible(self.CARD_FISH)
        self.drag_and_drop_on_to_element_new(self.CARD_FISH, self.SECOND_PACKAGE)

    def drag_card_monkey_in_package_on_three(self):
        self.element_is_visible(self.CARD_MONKEY)
        self.drag_and_drop_on_to_element_new(self.CARD_MONKEY, self.THIRD_PACKAGE)

    def drag_card_bird_in_package_in_nest(self):
        self.element_is_visible(self.CARD_BIRD)
        self.drag_and_drop_on_to_element_new(self.CARD_BIRD, self.FIRST_PACKAGE)

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()