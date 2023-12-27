from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class CountingObjectsLessonTakeKittenToBusStopPage(BasePage):
    INPUT = (By.XPATH, '//div[contains(@class, "focused")]')
    BUTTON_KEY_0 = (By.XPATH, '//div[@data-value="0"]')
    BUTTON_KEY_1 = (By.XPATH, '//div[@data-value="1"]')
    BUTTON_KEY_2 = (By.XPATH, '//div[@data-value="2"]')
    BUTTON_KEY_3 = (By.XPATH, '//div[@data-value="3"]')
    BUTTON_KEY_4 = (By.XPATH, '//div[@data-value="4"]')
    BUTTON_KEY_5 = (By.XPATH, '//div[@data-value="5"]')
    BUTTON_KEY_6 = (By.XPATH, '//div[@data-value="6"]')
    BUTTON_KEY_7 = (By.XPATH, '//div[@data-value="7"]')
    BUTTON_KEY_8 = (By.XPATH, '//div[@data-value="8"]')
    BUTTON_KEY_9 = (By.XPATH, '//div[@data-value="9"]')
    HOUSE_1 = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    HOUSE_2 = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    HOUSE_3 = (By.XPATH, '//div[@data-component-name="picBlockItem_2"]')
    HOUSE_4 = (By.XPATH, '//div[@data-component-name="picBlockItem_3"]')
    HOUSE_5 = (By.XPATH, '//div[@data-component-name="picBlockItem_4"]')
    HOUSE_6 = (By.XPATH, '//div[@data-component-name="picBlockItem_5"]')
    HOUSE_7 = (By.XPATH, '//div[@data-component-name="picBlockItem_6"]')


    def click_on_button_key_1_fill_input_1(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_1).click()

    def click_on_button_key_2_fill_input_2(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_2).click()

    def click_on_button_key_3_fill_input_3(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_3).click()

    def click_on_button_key_4_fill_input_4(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_4).click()

    def click_on_button_key_5_fill_input_5(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_5).click()

    def click_on_button_key_6_fill_input_6(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_6).click()

    def click_on_button_key_7_fill_input_7(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_7).click()

    def click_on_button_key_8_fill_input_8(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_8).click()

    def click_on_house_1(self):
        self.element_is_visible(self.HOUSE_1).click()
        self.element_is_invisible(self.HOUSE_1)

    def click_on_house_2(self):
        self.element_is_visible(self.HOUSE_2).click()
        self.element_is_invisible(self.HOUSE_2)

    def click_on_house_3(self):
        self.element_is_visible(self.HOUSE_3).click()
        self.element_is_invisible(self.HOUSE_3)

    def click_on_house_4(self):
        self.element_is_visible(self.HOUSE_4).click()
        self.element_is_invisible(self.HOUSE_4)

    def click_on_house_5(self):
        self.element_is_visible(self.HOUSE_5).click()
        self.element_is_invisible(self.HOUSE_5)


    def click_on_house_6(self):
        self.element_is_visible(self.HOUSE_6).click()
        self.element_is_invisible(self.HOUSE_6)

    def click_on_house_7(self):
        self.element_is_visible(self.HOUSE_7).click()
        self.element_is_invisible(self.HOUSE_7)

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()
