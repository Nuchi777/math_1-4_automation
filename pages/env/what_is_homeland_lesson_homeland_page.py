from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class WhatIsHomelandLessonHomelandPage(BasePage):
    CARD_CITY = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    CARD_DISTRICT = (By.XPATH, '//div[@data-component-name="picBlockItem_4"]')
    CARD_VILLAGE = (By.XPATH, '//div[@data-component-name="picBlockItem_2"]')
    CARD_HAMLET = (By.XPATH, '//div[@data-component-name="picBlockItem_5"]')
    BUTTON_DONE_ACTIVE = (By.XPATH, '//button[@data-component-name="button-done"]')
    BUTTON_DONE_DISABLED = (By.XPATH, '//button[contains(@class, "disabled")]')
    TEXT_BUTTON_CITY = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="город"]')
    TEXT_BUTTON_DISTRICT = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="район"]')
    TEXT_BUTTON_VILLAGE = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="деревня"]')
    TEXT_BUTTON_HAMLET = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="село"]')
    SLOT_EMPTY_FOCUSED = (By.XPATH, '//div[contains(@class, "focused")]')
    I_BORN_IN_VILLAGE_SUKHOVO = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    I_BORN_IN_OMSK = (By.XPATH, '//div[@data-component-name="picBlockItem_2"]')
    TEXT_BUTTON_SMALL_HOMELAND = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="малая родина"]')
    TEXT_BUTTON_HOMELAND = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="Родина"]')

    def click_on_city_card(self):
        self.element_is_visible(self.CARD_CITY).click()

    def click_on_district_card(self):
        self.element_is_visible(self.CARD_DISTRICT).click()

    def click_on_village_card(self):
        self.element_is_visible(self.CARD_VILLAGE).click()

    def click_on_hamlet_card(self):
        self.element_is_visible(self.CARD_HAMLET).click()

    def click_on_done_button(self):
        self.element_is_invisible(self.BUTTON_DONE_DISABLED)
        self.element_is_clickable(self.BUTTON_DONE_ACTIVE).click()

    def click_on_word_city(self):
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)
        self.element_is_clickable(self.TEXT_BUTTON_CITY).click()

    def click_on_word_district(self):
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)
        self.element_is_clickable(self.TEXT_BUTTON_DISTRICT).click()

    def click_on_word_village(self):
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)
        self.element_is_clickable(self.TEXT_BUTTON_VILLAGE).click()

    def click_on_word_hamlet(self):
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)
        self.element_is_clickable(self.TEXT_BUTTON_HAMLET).click()

    def click_on_card_i_born_in_village_sukhovo(self):
        self.element_is_visible(self.I_BORN_IN_VILLAGE_SUKHOVO).click()
        self.element_is_invisible(self.I_BORN_IN_VILLAGE_SUKHOVO)

    def click_on_card_i_born_in_omsk(self):
        self.element_is_visible(self.I_BORN_IN_OMSK).click()
        self.element_is_invisible(self.I_BORN_IN_OMSK)

    def click_on_word_small_homeland(self):
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)
        self.element_is_clickable(self.TEXT_BUTTON_SMALL_HOMELAND).click()

    def click_on_word_homeland(self):
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)
        self.element_is_clickable(self.TEXT_BUTTON_HOMELAND).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()
