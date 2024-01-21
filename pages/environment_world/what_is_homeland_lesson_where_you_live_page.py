import random
import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class WhatIsHomelandLessonWhereYouLivePage(BasePage):
    OBJECT_CITY = (By.XPATH, f'(//div[contains(@class, "ItemsGroup")]){[random.randint(1, 15)]}')
    AREA_CITY = (By.XPATH, '//div[contains(@class, "DropZone")]')
    BUTTON_DONE = (By.XPATH, '//div[@data-value="Enter"]')
    PRELOADER_DISABLED = (By.XPATH, '//div[contains(@class, "Preloader hide disabled")]')

    def drag_any_item_to_city_area(self):
        self.element_is_presence(self.PRELOADER_DISABLED)
        self.drag_and_drop_on_to_element_new(self.OBJECT_CITY, self.AREA_CITY)

    def click_on_done_button(self):
        self.element_is_clickable(self.BUTTON_DONE).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()
