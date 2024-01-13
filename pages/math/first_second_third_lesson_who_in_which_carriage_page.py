import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class FirstSecondThirdLessonWhoInWhichCarriagePage(BasePage):
    FIRST_CARRIAGE_CLICKABLE = (By.XPATH, '//div[@data-component-name="picBlockItem_1"]')
    FOURTH_CARRIAGE_CLICKABLE = (By.XPATH, '//div[@data-component-name="picBlockItem_4"]')
    ANIMALS = (By.XPATH, '//div[contains(@class, "DraggableItems")]')
    ANIMAL_ACTIVE = (By.XPATH, '//div[contains(@class, "undefined active")]')
    FIRST_CARRIAGE_DROPPABLE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[1]')
    SECOND_CARRIAGE_DROPPABLE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[2]')
    THIRD_CARRIAGE_DROPPABLE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[3]')
    FOURTH_CARRIAGE_DROPPABLE = (By.XPATH, '(//div[contains(@class, "DropContainer")])[4]')


    def click_on_first_carriage(self):
        self.element_is_visible(self.FIRST_CARRIAGE_CLICKABLE).click()
        self.element_is_invisible(self.FIRST_CARRIAGE_CLICKABLE)

    def click_on_fourth_carriage(self):
        self.element_is_visible(self.FOURTH_CARRIAGE_CLICKABLE).click()
        self.element_is_invisible(self.FOURTH_CARRIAGE_CLICKABLE)

    def drag_animal_in_third_carriage(self):
        self.element_is_visible(self.ANIMAL_ACTIVE)
        self.drag_and_drop_on_to_element_new(self.ANIMALS, self.THIRD_CARRIAGE_DROPPABLE)

    def drag_animal_in_first_carriage(self):
        self.element_is_visible(self.ANIMAL_ACTIVE)
        self.drag_and_drop_on_to_element_new(self.ANIMALS, self.FIRST_CARRIAGE_DROPPABLE)

    def drag_animal_in_second_carriage(self):
        self.element_is_visible(self.ANIMAL_ACTIVE)
        self.drag_and_drop_on_to_element_new(self.ANIMALS, self.SECOND_CARRIAGE_DROPPABLE)

    def drag_animal_in_fourth_carriage(self):
        self.element_is_visible(self.ANIMAL_ACTIVE)
        self.drag_and_drop_on_to_element_new(self.ANIMALS, self.FOURTH_CARRIAGE_DROPPABLE)

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()
