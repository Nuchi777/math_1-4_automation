import time
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class CosmicAdventureLessonExplorePlanetPage(BasePage):
    INPUT = (By.XPATH, '//div[contains(@class, "focused")]')
    BUTTON_KEY_3 = (By.XPATH, '//div[@data-value="3"]')
    BUTTON_KEY_2 = (By.XPATH, '//div[@data-value="2"]')
    BUTTON_KEY_4 = (By.XPATH, '//div[@data-value="4"]')
    BUTTON_KEY_5 = (By.XPATH, '//div[@data-value="5"]')
    NUMBER_7 = (By.XPATH, '//div[@data-component-name="picBlockItem_3"]')
    NUMBER_1 = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    NUMBER_5 = (By.XPATH, '//div[@data-component-name="picBlockItem_0"]')
    BUTTON_NEXT = (By.XPATH, '//div[contains(@class, "NextButton")]')
    CIFRYATA_ANIMATION = (By.XPATH, '//div[contains(@class, "startAnimation")]')
    CIFRYATA_LIST = [(By.CSS_SELECTOR, '#ClickObject'), (By.CSS_SELECTOR, '#ClickObject_2'),
                     (By.CSS_SELECTOR, '#ClickObject_3'), (By.CSS_SELECTOR, '#ClickObject_4'),
                     (By.CSS_SELECTOR, '#ClickObject_5')]
    PIC_BLOCK_3 = (By.XPATH, '//div[@data-component-name="picBlockItem_2"]')
    PIC_BLOCK_4 = (By.XPATH, '//div[@data-component-name="picBlockItem_3"]')
    SHUFFLE_DRAG_SORTER_HEAD_FISH = (By.XPATH, '(//div[@data-component-name="shuffle-drag-item"])[2]')
    SHUFFLE_DRAG_SORTER_HEAD_BODY_FISH = (By.XPATH, '(//div[@data-component-name="shuffle-drag-item"])[1]')
    SHUFFLE_DRAG_SORTER_BODY_FISH = (By.XPATH, '(//div[@data-component-name="shuffle-drag-item"])[4]')
    SHUFFLE_DRAG_SORTER_TAIL_FISH = (By.XPATH, '(//div[@data-component-name="shuffle-drag-item"])[3]')
    BUTTON_DONE = (By.XPATH, '//button[contains(@class, "ButtonDone")]')



    def click_on_button_key_3_fill_input_3(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_3).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_2_fill_input_2(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_2).click()
        self.element_is_invisible(self.INPUT)

    def click_on_button_key_4_fill_input_4(self):
        self.element_is_visible(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_4).click()


    def click_on_number_seven(self):
        self.element_is_visible(self.NUMBER_7).click()
        self.element_is_invisible(self.NUMBER_7)

    def click_on_number_one(self):
        self.element_is_visible(self.NUMBER_1).click()
        self.element_is_invisible(self.NUMBER_1)

    def click_on_number_five(self):
        self.element_is_visible(self.NUMBER_5).click()

    def click_on_next_button(self):
        self.element_is_visible(self.BUTTON_NEXT).click()

    def click_on_cifryts(self):
        self.element_is_visible(self.CIFRYATA_ANIMATION)
        self.element_is_invisible(self.CIFRYATA_ANIMATION)
        for i in self.CIFRYATA_LIST:
            self.element_is_visible(i).click()

    def click_on_button_key_5_fill_input(self):
        self.element_is_clickable(self.INPUT)
        self.element_is_visible(self.BUTTON_KEY_5).click()

    def click_on_pic_block_button_number_3(self):
        self.element_is_visible(self.PIC_BLOCK_3).click()
        self.element_is_invisible(self.PIC_BLOCK_3)

    def click_on_pic_block_button_number_4(self):
        self.element_is_visible(self.PIC_BLOCK_4).click()

    def drag_wrapper_heat_to_first_position(self):
        self.drag_and_drop_on_to_element(self.SHUFFLE_DRAG_SORTER_HEAD_FISH, self.SHUFFLE_DRAG_SORTER_HEAD_BODY_FISH)

    def drag_wrapper_tail_to_last_position(self):
        self.drag_and_drop_on_to_element(self.SHUFFLE_DRAG_SORTER_BODY_FISH, self.SHUFFLE_DRAG_SORTER_TAIL_FISH)

    def click_on_done_button(self):
        time.sleep(1)
        self.element_is_clickable(self.BUTTON_DONE).click()

    def check_table_marathon_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.TABLE_MARATHON).is_displayed()





