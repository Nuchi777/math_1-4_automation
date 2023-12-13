import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CosmicAdventureLessonFixRocketPage(BasePage):
    BUTTON_PLAY = (By.XPATH, '//div[contains(@class, "StyledButtonWrap")]')

    def click_on_button_play(self):
        self.element_is_visible(self.BUTTON_PLAY).click()
