from locators.main_profile_students_page_locators import MainProfileStudentsPageLocators
from pages.base_page import BasePage


class MainProfileStudentsPage(BasePage):
    locators = MainProfileStudentsPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_card_math(self):
        self.element_is_visible(self.locators.LESSON_CARD_MATH).click()
