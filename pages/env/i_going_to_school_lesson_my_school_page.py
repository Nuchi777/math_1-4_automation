import time
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class IGoingToSchoolLessonMySchoolPage(BasePage):
    FIRST_PACKAGE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[1]')
    SECOND_PACKAGE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[2]')
    THIRD_PACKAGE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[3]')
    FIRST_CARD = (By.XPATH, '(//div[contains(@class, "DraggableItemContainer")])[1]')
    SECOND_CARD = (By.XPATH, '(//div[contains(@class, "DraggableItemContainer")])[2]')
    THIRD_CARD = (By.XPATH, '(//div[contains(@class, "DraggableItemContainer")])[3]')
    STACK_OF_CARDS = (By.XPATH, '//div[contains(@class, "DraggableItemContainer")]')

    def drag_card_in_classroom_izo_in_draw_package(self):
        self.element_is_visible(self.FIRST_CARD)
        self.drag_and_drop_on_to_element_new(self.FIRST_CARD, self.THIRD_PACKAGE)
        self.element_is_invisible(self.FIRST_CARD)

    def drag_card_in_dining_room_in_eating_package(self):
        self.element_is_visible(self.SECOND_CARD)
        self.drag_and_drop_on_to_element_new(self.SECOND_CARD, self.FIRST_PACKAGE)
        self.element_is_invisible(self.SECOND_CARD)

    def drag_card_in_library_in_reading_books_package(self):
        self.element_is_visible(self.THIRD_CARD)
        self.drag_and_drop_on_to_element_new(self.THIRD_CARD, self.SECOND_PACKAGE)
        self.element_is_invisible(self.SECOND_PACKAGE)

    def drag_card_in_classroom_in_learning_package(self):
        self.element_is_visible(self.FIRST_CARD)
        self.drag_and_drop_on_to_element_new(self.FIRST_CARD, self.FIRST_PACKAGE)
        self.element_is_invisible(self.FIRST_CARD)

    def drag_card_in_wardrobe_in_undress_package(self):
        self.element_is_visible(self.SECOND_CARD)
        self.drag_and_drop_on_to_element_new(self.SECOND_CARD, self.THIRD_PACKAGE)
        self.element_is_invisible(self.SECOND_CARD)

    def drag_card_in_gym_in_run_package(self):
        self.element_is_visible(self.THIRD_CARD)
        self.drag_and_drop_on_to_element_new(self.THIRD_CARD, self.SECOND_PACKAGE)
        self.element_is_invisible(self.SECOND_PACKAGE)

    def drag_card_hustle_in_cannot_package(self):
        self.drag_and_drop_on_to_element_new(self.STACK_OF_CARDS, self.SECOND_PACKAGE)

    def drag_card_ride_on_railing_in_cannot_package(self):
        self.drag_and_drop_on_to_element_new(self.STACK_OF_CARDS, self.SECOND_PACKAGE)

    def drag_card_help_in_can_package(self):
        self.drag_and_drop_on_to_element_new(self.STACK_OF_CARDS, self.FIRST_PACKAGE)

    def drag_card_greet_in_can_package(self):
        self.drag_and_drop_on_to_element_new(self.STACK_OF_CARDS, self.FIRST_PACKAGE)

    def drag_card_fight_in_cannot_package(self):
        self.drag_and_drop_on_to_element_new(self.STACK_OF_CARDS, self.SECOND_PACKAGE)

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()

