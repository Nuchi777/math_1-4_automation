from locators.math_study_topic_page_locators import MathStudyTopicPageLocators
from pages.base_page import BasePage


class MathStudyTopicPage(BasePage):

    locators = MathStudyTopicPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_cosmic_adventure_lesson(self):
        self.element_is_visible(self.locators.LESSON_COSMIC_ADVENTURE).click()

    def click_on_play_button(self):
        self.element_is_visible(self.locators.PLAY_BUTTON_CARD).click()



