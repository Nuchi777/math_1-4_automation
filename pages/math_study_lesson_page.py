from locators.math_study_lesson_page_locators import MathStudyLessonPageLocators
from pages.base_page import BasePage


class MathStudyLessonPage(BasePage):

    locators = MathStudyLessonPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_card_start(self):
        self.element_is_visible(self.locators.CARD_PREVIEW_START).click()