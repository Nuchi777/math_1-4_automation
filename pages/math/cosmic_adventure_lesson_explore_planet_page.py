import time
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class CosmicAdventureLessonExplorePlanetPage(BasePage):
    INPUT = (By.XPATH, '//div[contains(@class, "styles__StyledPrimaryInputInner-sc")]')
    INPUT_2 = (By.XPATH, '(//div[contains(@class, "styles__StyledPrimaryInputInner-sc")])[1]')
    INPUT_4 = (By.XPATH, '(//div[contains(@class, "styles__StyledPrimaryInputInner-sc")])[2]')
    BUTTON_KEY_3 = (By.XPATH, '//div[contains(@class, "styles__StyledKey-sc")][text()="3"]')
    BUTTON_KEY_2 = (By.XPATH, '//div[contains(@class, "styles__StyledKey-sc")][text()="2"]')
    BUTTON_KEY_4 = (By.XPATH, '//div[contains(@class, "styles__StyledKey-sc")][text()="4"]')
    BUTTON_KEY_5 = (By.XPATH, '//div[contains(@class, "styles__StyledKey-sc")][text()="5"]')
    NUMBER_7 = (By.XPATH, '//div[@data-component-name="picBlockItem_3"]')
    NUMBER_1 = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    NUMBER_5 = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    BUTTON_NEXT = (By.XPATH, '//div[contains(@class, "styles__StyledNextButton-sc")]')
    CIFRYATA_LIST = [(By.CSS_SELECTOR, '#ClickObject'), (By.CSS_SELECTOR, '#ClickObject_2'),
                     (By.CSS_SELECTOR, '#ClickObject_3'), (By.CSS_SELECTOR, '#ClickObject_4'),
                     (By.CSS_SELECTOR, '#ClickObject_5')]
    PIC_BLOCK_3 = (By.XPATH, '//div[@data-component-name="picBlockItem_2"]')
    PIC_BLOCK_4 = (By.XPATH, '//div[@data-component-name="picBlockItem_3"]')
    SHUFFLE_DRAG_SORTER_HEAD_FISH = (By.XPATH, '(//div[@class="styles__StyledWrapper-sc-1x77hkp-0 iGdZUz"])[2]')
    SHUFFLE_DRAG_SORTER_HEAD_BODY_FISH = (By.XPATH, '(//div[@class="styles__StyledWrapper-sc-1x77hkp-0 iGdZUz"])[1]')
    SHUFFLE_DRAG_SORTER_BODY_FISH = (By.XPATH, '(//div[@class="styles__StyledWrapper-sc-1x77hkp-0 iGdZUz"])[4]')
    SHUFFLE_DRAG_SORTER_TAIL_FISH = (By.XPATH, '(//div[@class="styles__StyledWrapper-sc-1x77hkp-0 iGdZUz"])[3]')
    BUTTON_DONE = (By.XPATH, '//button[contains(@class, "StyledButtonDone")]')
    PROGRESS_BAR_CHUNK_1 = (By.XPATH, '//div[@width="53.269230769230774"]')
    PROGRESS_BAR_CHUNK_3 = (By.XPATH, '//div[@width="114.8076923076923"]')
    PROGRESS_BAR_CHUNK_4 = (By.XPATH, '//div[@width="145.5769230769231"]')
    PROGRESS_BAR_CHUNK_7 = (By.XPATH, '//div[@width="299.4230769230769"]')



    def click_on_button_key_3_fill_input_3(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_3).click()

    def click_on_button_key_2_fill_input_2(self):
        self.element_is_visible(self.PROGRESS_BAR_CHUNK_1)
        self.element_is_visible(self.INPUT_2)
        self.element_is_visible(self.BUTTON_KEY_2).click()

    def click_on_button_key_4_fill_input_4(self):
        self.element_is_clickable(self.INPUT_4)
        self.element_is_visible(self.BUTTON_KEY_4).click()

    def click_on_number_seven(self):
        self.element_is_visible(self.NUMBER_7).click()

    def click_on_number_one(self):
        self.element_is_visible(self.PROGRESS_BAR_CHUNK_3)
        self.element_is_visible(self.NUMBER_1).click()

    def click_on_number_five(self):
        self.element_is_visible(self.PROGRESS_BAR_CHUNK_4)
        self.element_is_visible(self.NUMBER_5).click()

    def click_on_next_button(self):
        self.element_is_visible(self.BUTTON_NEXT).click()

    def click_on_cifryts(self):
        time.sleep(5)
        for i in self.CIFRYATA_LIST:
            self.element_is_visible(i).click()

    def click_on_button_key_5_fill_input(self):
        self.element_is_clickable(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_5).click()

    def click_on_pic_block_button_number_3(self):
        self.element_is_visible(self.PIC_BLOCK_3).click()

    def click_on_pic_block_button_number_4(self):
        self.element_is_visible(self.PROGRESS_BAR_CHUNK_7)
        self.element_is_visible(self.PIC_BLOCK_4).click()

    def drag_wrapper_heat_to_first_position(self):
        self.drag_and_drop_on_to_element(self.SHUFFLE_DRAG_SORTER_HEAD_FISH, self.SHUFFLE_DRAG_SORTER_HEAD_BODY_FISH)

    def drag_wrapper_tail_to_last_position(self):
        self.drag_and_drop_on_to_element(self.SHUFFLE_DRAG_SORTER_BODY_FISH, self.SHUFFLE_DRAG_SORTER_TAIL_FISH)

    def click_on_done_button(self):
        time.sleep(1)
        self.element_is_visible(self.BUTTON_DONE).click()

    def check_table_marathon_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.TABLE_MARATHON).is_displayed()





