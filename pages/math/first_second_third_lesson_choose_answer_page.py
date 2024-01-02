import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class FirstSecondThirdLessonChooseAnswerPage(BasePage):
    BUTTON_THREE = (By.XPATH, '//div[@data-choice-button-id="1"]')
    BUTTON_SECOND = (By.XPATH, '//div[@data-choice-button-id="0"]')
    BUTTON_FIVE = (By.XPATH, '//div[@data-choice-button-id="2"]')
    BUTTON_IN_FOURTH = (By.XPATH, '//div[@data-choice-button-id="0"]')

    def click_on_three_button(self):
        self.element_is_visible(self.BUTTON_THREE).click()
        self.element_is_invisible(self.BUTTON_THREE)

    def click_on_second_button(self):
        self.element_is_visible(self.BUTTON_SECOND).click()
        self.element_is_invisible(self.BUTTON_SECOND)

    def click_on_five_button(self):
        self.element_is_visible(self.BUTTON_FIVE).click()
        self.element_is_invisible(self.BUTTON_FIVE)

    def click_on_in_fourth_button(self):
        self.element_is_visible(self.BUTTON_IN_FOURTH).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()