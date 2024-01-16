import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class SpeechAndLanguageLessonLearningVocabularyWordsPage(BasePage):
    FIRST_LETTER_O = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    WORD_GOROD = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    LETTER_G = (By.XPATH, '//div[contains(@class, "state_default")]/div[text()="г"]')
    LETTER_O = (By.XPATH, '//div[contains(@class, "state_default")]/div[text()="о"]')
    LETTER_R = (By.XPATH, '//div[contains(@class, "state_default")]/div[text()="р"]')
    LETTER_D = (By.XPATH, '//div[contains(@class, "state_default")]/div[text()="д"]')
    BUTTON_DONE = (By.XPATH, '//button[contains(@class, "DoneButton")]')
    FOCUSED = (By.XPATH, '//div[contains(@class, "focused")]')

    def click_on_first_letter_o(self):
        self.element_is_clickable(self.FIRST_LETTER_O).click()
        self.element_is_invisible(self.FIRST_LETTER_O)

    def click_on_option_gorod(self):
        self.element_is_visible(self.WORD_GOROD).click()

    def click_on_letter_g(self):
        self.element_is_visible(self.FOCUSED)
        self.element_is_visible(self.LETTER_G).click()

    def click_on_letter_o(self):
        self.element_is_visible(self.LETTER_O).click()

    def click_on_letter_r(self):
        self.element_is_visible(self.LETTER_R).click()

    def click_on_letter_d(self):
        self.element_is_visible(self.LETTER_D).click()

    def click_on_button_done(self):
        self.element_is_clickable(self.BUTTON_DONE).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()