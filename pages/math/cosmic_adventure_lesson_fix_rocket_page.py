from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class CosmicAdventureLessonFixRocketPage(BasePage):
    BUTTON_PLAY = (By.XPATH, '//div[contains(@class, "ButtonWrap")]')
    BUTTON_NEXT = (By.XPATH, '//div[contains(@class, "NextButton")]')
    BOX_THREE_STONES = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    BOX_ONE_STONES = (By.XPATH, '//div[@data-component-name="picBlockItem_4"]')
    ZAVR_FOUR_STONES = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    ZAVR_THREE_STONES = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    ELEMENT_ROCKET = (By.XPATH, '//div[contains(@class,"DraggableItems")]')
    ROCKET = (By.XPATH, '//div[contains(@class,"DropContainer")]')


    def click_on_button_play(self):
        self.element_is_visible(self.BUTTON_PLAY).click()

    def click_on_box_with_three_stones(self):
        self.element_is_visible(self.BOX_THREE_STONES).click()
        self.element_is_invisible(self.BOX_THREE_STONES)

    def click_on_box_with_one_stone(self):
        self.element_is_visible(self.BOX_ONE_STONES).click()
        self.element_is_invisible(self.BOX_ONE_STONES)

    def click_on_zavrik_with_four_stones(self):
        self.element_is_visible(self.ZAVR_FOUR_STONES).click()
        self.element_is_invisible(self.ZAVR_FOUR_STONES)

    def click_on_zavrik_with_three_stones(self):
        self.element_is_visible(self.ZAVR_THREE_STONES).click()

    def click_on_next_button(self):
        self.element_is_visible(self.BUTTON_NEXT).click()

    def drag_rocket_element_to_rocket(self):
        self.drag_and_drop_on_to_element_new(self.ELEMENT_ROCKET, self.ROCKET)

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()


