from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class SpeechAndLanguageLessonWhyIsSpeechNeededPage(BasePage):
    BUTTON_ASK = (By.XPATH, '//span[text()="просят"]')
    BUTTON_TELL = (By.XPATH, '//span[text()="рассказывают"]')
    BUTTON_QUESTION = (By.XPATH, '//span[text()="спрашивают"]')
    FIRST_CARD = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    SECOND_CARD = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    THIRD_CARD = (By.XPATH, '//div[@data-component-name="picBlockItem_2"]')

    def click_on_button_question(self):
        self.element_is_visible(self.BUTTON_QUESTION).click()

    def click_on_button_tell(self):
        self.element_is_visible(self.BUTTON_TELL).click()

    def click_on_button_ask(self):
        self.element_is_visible(self.BUTTON_ASK).click()

    def click_on_first_card(self):
        self.element_is_visible(self.FIRST_CARD).click()
        self.element_is_invisible(self.FIRST_CARD)

    def click_on_third_card(self):
        self.element_is_visible(self.THIRD_CARD).click()
        self.element_is_invisible(self.THIRD_CARD)

    def click_on_second_card(self):
        self.element_is_visible(self.SECOND_CARD).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()


