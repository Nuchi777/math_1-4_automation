import time
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class CosmicAdventureLessonExplorePlanetPage(BasePage):
    INPUT_3 = (By.XPATH, '//div[contains(@class, "styles__StyledPrimaryInputInner-sc")]')
    BUTTON_KEY_3 = (By.XPATH, '//div[contains(@class, "styles__StyledKey-sc")][text()="3"]')

    def click_on_button_key_3_fill_input_3(self):
        self.element_is_clickable(self.INPUT_3)
        self.element_is_visible(self.BUTTON_KEY_3).click()