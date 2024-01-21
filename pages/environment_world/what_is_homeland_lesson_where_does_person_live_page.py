from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class WhatIsHomelandLessonWhereDoesPersonLivePage(BasePage):
    BUTTON_HOMELAND = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    BUTTON_RUSSIA = (By.XPATH, '//div[@data-component-name="picBlockItem_3"]')
    BUTTON_USA = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    TEXT_BUTTON_HOMELAND = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="Родина"]')
    SLOT_EMPTY_FOCUSED = (By.XPATH, '//div[contains(@class, "focused")]')

    def click_on_homeland_button(self):
        self.element_is_visible(self.BUTTON_HOMELAND).click()

    def click_on_russia_button(self):
        self.element_is_visible(self.BUTTON_RUSSIA).click()
        self.element_is_invisible(self.BUTTON_RUSSIA)

    def click_on_usa_button(self):
        self.element_is_visible(self.BUTTON_USA).click()
        self.element_is_invisible(self.BUTTON_USA)

    def click_on_word_homeland(self):
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)
        self.element_is_clickable(self.TEXT_BUTTON_HOMELAND).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()
