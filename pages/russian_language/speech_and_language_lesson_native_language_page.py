import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class SpeechAndLanguageLessonNativeLanguagePage(BasePage):
    FIRST_PHOTO_KALMYKIA_STATE_DEFAULT = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    FIRST_PHOTO_KALMYKIA_STATE_SUCCESS = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]/div[contains(@class, "state_success")]')
    SECOND_PHOTO_CHUVASHIA_STATE_DEFAULT = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    SECOND_PHOTO_CHUVASHIA_STATE_SUCCESS = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]/div[contains(@class, "state_success")]')
    THIRD_PHOTO_BASHKORTOSTAN_STATE_DEFAULT = (By.XPATH, '//div[@data-component-name="picBlockItem_7"]')
    THIRD_PHOTO_BASHKORTOSTAN_STATE_SUCCESS = (By.XPATH, '//div[@data-component-name="picBlockItem_7"]/div[contains(@class, "state_success")]')
    FOURTH_PHOTO_YAKUTIA_STATE_DEFAULT = (By.XPATH, '//div[@data-component-name="picBlockItem_4"]')
    FOURTH_PHOTO_YAKUTIA_STATE_SUCCESS = (By.XPATH, '//div[@data-component-name="picBlockItem_4"]/div[contains(@class, "state_success")]')
    BUTTON_KALMYK = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="калмыцкий"]')
    BUTTON_CHUVASH = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="чувашский"]')
    BUTTON_YAKUT = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="якутский"]')
    BUTTON_BASHKIR = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="башкирский"]')
    BUTTON_NATIVE_LANGUAGE = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="родной язык"]')
    BUTTON_RUSSIAN_LANGUAGE = (By.XPATH, '//div[contains(@class, "PlateElem")]/div[text()="русский язык"]')
    SLOT_EMPTY_FOCUSED = (By.XPATH, '//div[contains(@class, "focused")]')

    def click_on_first_photo_kalmykia(self):
        self.element_is_clickable(self.FIRST_PHOTO_KALMYKIA_STATE_DEFAULT).click()
        self.element_is_visible(self.FIRST_PHOTO_KALMYKIA_STATE_SUCCESS)

    def click_on_second_photo_chuvashia(self):
        self.element_is_clickable(self.SECOND_PHOTO_CHUVASHIA_STATE_DEFAULT).click()
        self.element_is_visible(self.SECOND_PHOTO_CHUVASHIA_STATE_SUCCESS)

    def click_on_third_photo_Bashkortostan(self):
        self.element_is_clickable(self.THIRD_PHOTO_BASHKORTOSTAN_STATE_DEFAULT).click()
        self.element_is_visible(self.THIRD_PHOTO_BASHKORTOSTAN_STATE_SUCCESS)

    def click_on_fourth_photo_yakutia(self):
        self.element_is_clickable(self.FOURTH_PHOTO_YAKUTIA_STATE_DEFAULT).click()
        self.element_is_visible(self.FOURTH_PHOTO_YAKUTIA_STATE_SUCCESS)

    def click_on_option_kalmyk(self):
        self.element_is_clickable(self.BUTTON_KALMYK).click()
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)

    def click_on_option_chuvash(self):
        self.element_is_clickable(self.BUTTON_CHUVASH).click()
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)

    def click_on_option_yakut(self):
        self.element_is_clickable(self.BUTTON_YAKUT).click()
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)

    def click_on_option_bashkir(self):
        self.element_is_clickable(self.BUTTON_BASHKIR).click()
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)

    def click_on_option_native_language(self):
        self.element_is_clickable(self.BUTTON_NATIVE_LANGUAGE).click()
        self.element_is_visible(self.SLOT_EMPTY_FOCUSED)

    def click_on_option_russian_language(self):
        self.element_is_clickable(self.BUTTON_RUSSIAN_LANGUAGE).click()

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()

