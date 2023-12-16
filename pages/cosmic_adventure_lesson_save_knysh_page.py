import random
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class CosmicAdventureLessonSaveKnyshPage(BasePage):
    BUTTON_PLAY = (By.XPATH, '//div[contains(@class, "StyledButtonWrap")]')
    BUTTON_NEXT = (By.XPATH, '//div[contains(@class, "styles__StyledNextButton-sc")]')
    INPUT_1 = (By.XPATH, '(//div[contains(@class, "InputInner")])[1]')
    INPUT_2 = (By.XPATH, '(//div[contains(@class, "InputInner")])[2]')
    INPUT_3 = (By.XPATH, '(//div[contains(@class, "InputInner")])[3]')
    BUTTON_KEY_6 = (By.XPATH, '//div[@data-value="6"]')
    BUTTON_KEY_7 = (By.XPATH, '//div[@data-value="7"]')
    BUTTON_KEY_1 = (By.XPATH, '//div[@data-value="1"]')
    BUTTON_KEY_0 = (By.XPATH, '//div[@data-value="0"]')
    ELEMENT_ROCKET = (By.XPATH, f'(//div[contains(@class, "ItemsGroup")]){[random.randint(1,16)]}')
    ROCKET = (By.XPATH, '//div[contains(@class, "DropZoneContainer")]')
    BUTTON_DONE = (By.XPATH, '//div[contains(@class, "EnterKeyInner")]')
    BUTTON_CONTINUE_TO_STUDY = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')


    def click_on_button_play(self):
        self.element_is_visible(self.BUTTON_PLAY).click()

    def click_on_next_button(self):
        self.element_is_visible(self.BUTTON_NEXT).click()

    def click_on_button_key_6_fill_input_1(self):
        self.element_is_visible(self.INPUT_1)
        self.element_is_visible(self.BUTTON_KEY_6).click()

    def click_on_button_key_7_fill_input_2(self):
        self.element_is_visible(self.INPUT_2)
        self.element_is_visible(self.BUTTON_KEY_7).click()

    def click_on_button_key_1_and_0_fill_input_3(self):
        self.element_is_visible(self.INPUT_3)
        self.element_is_visible(self.BUTTON_KEY_1).click()
        self.element_is_visible(self.BUTTON_KEY_0).click()

    def drag_rocket_element_to_rocket(self):
        self.drag_and_drop_on_to_element_new(self.ELEMENT_ROCKET, self.ROCKET)

    def click_on_done_button(self):
        self.element_is_visible(self.BUTTON_DONE).click()

    def click_on_button_continue_to_study(self):
        self.element_is_visible(self.BUTTON_CONTINUE_TO_STUDY).click()

    def check_title_base_course_finish_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.TITLE_BASE_COURSE_FINISH).is_displayed()