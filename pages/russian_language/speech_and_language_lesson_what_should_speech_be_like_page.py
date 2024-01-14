import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class SpeechAndLanguageLessonWhatShouldSpeechBeLikePage(BasePage):
    FIRST_CLICKABLE_CARD = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    FIRST_DRAGGABLE_CARD = (By.XPATH, '(//div[contains(@class, "SlotContainer")])[1]')
    DRAGGABLE_ITEM = (By.XPATH, '//div[contains(@class, "DraggableItem")]')
    BUTTON_POLITELY = (By.XPATH, '//span[text()="вежливо"]')
    BUTTON_ACCESSIBLY = (By.XPATH, '//span[text()="понятно"]')
    BUTTON_CORRECTLY = (By.XPATH, '//span[text()="грамотно"]')
    BUTTON_UNDERSTANDABLE = (By.XPATH, '//span[text()="понятной"]')
    BUTTON_LITERATE = (By.XPATH, '//span[text()="грамотной"]')
    BUTTON_POLITE = (By.XPATH, '//span[text()="вежливой"]')

    def click_on_look_how_beautiful_their_puppy(self):
        self.element_is_visible(self.FIRST_CLICKABLE_CARD).click()
        self.element_is_invisible(self.FIRST_CLICKABLE_CARD)

    def click_on_hello_lets_play_chess(self):
        self.element_is_visible(self.FIRST_CLICKABLE_CARD).click()

    def drag_apple_on_give_me_apple_please(self):
        time.sleep(1)
        self.drag_and_drop_on_to_element_new(self.DRAGGABLE_ITEM, self.FIRST_DRAGGABLE_CARD)
        self.element_is_invisible(self.DRAGGABLE_ITEM)

    def drag_candy_on_please_treat_me_to_some_candy(self):
        time.sleep(1)
        self.drag_and_drop_on_to_element_new(self.DRAGGABLE_ITEM, self.FIRST_DRAGGABLE_CARD)
        self.element_is_invisible(self.DRAGGABLE_ITEM)

    def drag_flashlight_on_give_me_flashlight(self):
        time.sleep(1)
        self.drag_and_drop_on_to_element_new(self.DRAGGABLE_ITEM, self.FIRST_DRAGGABLE_CARD)
        self.element_is_invisible(self.DRAGGABLE_ITEM)

    def drag_mug_on_give_me_mug(self):
        time.sleep(1)
        self.drag_and_drop_on_to_element_new(self.DRAGGABLE_ITEM, self.FIRST_DRAGGABLE_CARD)

    def click_on_button_politely(self):
        self.element_is_visible(self.BUTTON_POLITELY).click()

    def click_on_button_accessibly(self):
        self.element_is_visible(self.BUTTON_ACCESSIBLY).click()

    def click_on_button_correctly(self):
        self.element_is_visible(self.BUTTON_CORRECTLY).click()

    def click_on_button_understandable(self):
        self.element_is_visible(self.BUTTON_UNDERSTANDABLE).click()

    def click_on_button_literate(self):
        self.element_is_visible(self.BUTTON_LITERATE).click()

    def click_on_button_polite(self):
        self.element_is_visible(self.BUTTON_POLITE).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()
