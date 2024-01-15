import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class SpeechAndLanguageLessonWhatIsSpeechPage(BasePage):
    FIST_CARD = (By.XPATH, '(//div[contains(@class, "DraggableItems")]/div[contains(@class, "ItemContainer")])[1]')
    SECOND_CARD = (By.XPATH, '(//div[contains(@class, "DraggableItems")]/div[contains(@class, "ItemContainer")])[2]')
    THIRD_CARD = (By.XPATH, '(//div[contains(@class, "DraggableItems")]/div[contains(@class, "ItemContainer")])[3]')
    FIRST_PACKAGE_DROPPABLE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[1]')
    SECOND_PACKAGE_DROPPABLE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[2]')
    THIRD_PACKAGE_DROPPABLE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[3]')
    BUTTON_SPEAK = (By.XPATH, '//span[text()="говорить"]')
    BUTTON_HUMANS = (By.XPATH, '//span[text()="люди"]')

    def drag_cat_in_package_meows(self):
        time.sleep(1)
        self.element_is_clickable(self.FIST_CARD)
        self.drag_and_drop_on_to_element_new(self.FIST_CARD, self.THIRD_PACKAGE_DROPPABLE)

    def drag_human_in_package_speaks(self):
        self.drag_and_drop_on_to_element_new(self.SECOND_CARD, self.FIRST_PACKAGE_DROPPABLE)

    def drag_dog_in_package_barks(self):
        self.drag_and_drop_on_to_element_new(self.THIRD_CARD, self.SECOND_PACKAGE_DROPPABLE)
        self.element_is_invisible(self.FIRST_PACKAGE_DROPPABLE)

    def drag_mewing_in_package_with_cat(self):
        self.element_is_clickable(self.FIST_CARD)
        self.drag_and_drop_on_to_element_new(self.FIST_CARD, self.THIRD_PACKAGE_DROPPABLE)

    def drag_speech_in_package_with_human(self):
        self.drag_and_drop_on_to_element_new(self.SECOND_CARD, self.FIRST_PACKAGE_DROPPABLE)

    def drag_bark_in_package_with_dog(self):
        self.drag_and_drop_on_to_element_new(self.THIRD_CARD, self.SECOND_PACKAGE_DROPPABLE)

    def click_on_button_speak(self):
        self.element_is_visible(self.BUTTON_SPEAK).click()
        self.element_is_invisible(self.BUTTON_SPEAK)

    def click_on_button_humans(self):
        self.element_is_visible(self.BUTTON_HUMANS).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()