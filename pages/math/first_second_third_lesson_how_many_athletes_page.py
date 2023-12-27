import time

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class FirstSecondThirdLessonHowManyAthletesPage(BasePage):
    PRELOADER_DISABLED = (By.XPATH, '//div[@class="containerPreloader hide disabled"]')
    FIRST_BASKET = (By.XPATH, '(//div[contains(@class, "DropContainer")])[1]')
    SECOND_BASKET = (By.XPATH, '(//div[contains(@class, "DropContainer")])[2]')
    THIRD_BASKET = (By.XPATH, '(//div[contains(@class, "DropContainer")])[3]')
    FOURTH_BASKET = (By.XPATH, '(//div[contains(@class, "DropContainer")])[4]')
    FOOD = (By.XPATH, '//div[contains(@class, "DraggableItemContainer")]')
    ORDER_TEA = (By.XPATH, '//div[contains(@class, "DraggableItemContainer")]//*[@id="Property 1=6"]')
    ORDER_FRENCH_FRIES = (By.XPATH, '//div[contains(@class, "DraggableItemContainer")]//*[@id="Property 1=3"]')
    ORDER_ICE_CREAM = (By.XPATH, '//div[contains(@class, "DraggableItemContainer")]//*[@id="Property 1=1"]')
    ORDER_BURGER = (By.XPATH, '//div[contains(@class, "DraggableItemContainer")]//*[@id="Property 1=5"]')
    ORDER_CAKE = (By.XPATH, '//div[contains(@class, "DraggableItemContainer")]//*[@id="Property 1=2"]')
    ORDER_CHICKEN_LEG = (By.XPATH, '//div[contains(@class, "DraggableItemContainer")]//*[@id="Property 1=4"]')

    def drag_cheese_to_basket_cheese(self):
        self.element_is_presence(self.PRELOADER_DISABLED)
        time.sleep(1)
        self.drag_and_drop_on_to_element_new(self.FOOD, self.THIRD_BASKET)

    def drag_bread_to_first_basket_buns(self):
        self.drag_and_drop_on_to_element_new(self.FOOD, self.FIRST_BASKET)

    def drag_salade_to_basket_salade(self):
        self.drag_and_drop_on_to_element_new(self.FOOD, self.SECOND_BASKET)

    def drag_four_chicken_legs_to_basket_by_four(self):
        self.element_is_invisible(self.THIRD_BASKET)
        self.element_is_presence(self.PRELOADER_DISABLED)
        time.sleep(2)
        self.drag_and_drop_on_to_element_new(self.FOOD, self.FIRST_BASKET)

    def drag_three_chicken_legs_to_basket_by_three(self):
        self.drag_and_drop_on_to_element_new(self.FOOD, self.SECOND_BASKET)

    def drag_order_tea_to_second_tray(self):
        self.element_is_visible(self.FOURTH_BASKET)
        self.element_is_presence(self.PRELOADER_DISABLED)
        time.sleep(1)
        self.drag_and_drop_on_to_element_new(self.ORDER_TEA, self.SECOND_BASKET)

    def drag_order_french_fries_to_third_tray(self):
        self.drag_and_drop_on_to_element_new(self.ORDER_FRENCH_FRIES, self.THIRD_BASKET)

    def drag_order_ice_cream_to_first_tray(self):
        self.drag_and_drop_on_to_element_new(self.ORDER_ICE_CREAM, self.FIRST_BASKET)

    def drag_order_burger_to_second_tray(self):
        self.drag_and_drop_on_to_element_new(self.ORDER_BURGER, self.SECOND_BASKET)

    def drag_order_cake_to_fourth_tray(self):
        self.drag_and_drop_on_to_element_new(self.ORDER_CAKE, self.FOURTH_BASKET)

    def drag_order_chicken_leg_to_third_tray(self):
        self.drag_and_drop_on_to_element_new(self.ORDER_CHICKEN_LEG, self.THIRD_BASKET)

    def drag_order_first_bag_to_third_tray(self):
        self.element_is_invisible(self.FOURTH_BASKET)
        self.element_is_presence(self.PRELOADER_DISABLED)
        time.sleep(2)
        self.drag_and_drop_on_to_element_new(self.FOOD, self.THIRD_BASKET)

    def drag_order_second_bag_to_first_tray(self):
        self.drag_and_drop_on_to_element_new(self.FOOD, self.FIRST_BASKET)

    def drag_order_third_bag_to_second_tray(self):
        self.drag_and_drop_on_to_element_new(self.FOOD, self.SECOND_BASKET)

    def check_headbar_logo_is_displayed(self):
        assert self.element_is_visible(MainPageLocators.HEADBAR_LOGO).is_displayed()
