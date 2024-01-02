import time
from pages.math.first_second_third_lesson_how_many_athletes_page import FirstSecondThirdLessonHowManyAthletesPage
from pages.math.first_second_third_lesson_poryadkovye_chislitelnye_page import FirstSecondThirdLessonPoryadkovyeChislitelnyePage
from pages.math.first_second_third_lesson_who_in_which_carriage_page import FirstSecondThirdLessonWhoInWhichCarriagePage
from data import UrlsFirstSecondThird


class TestMathFirstSecondThird:

    def test_math_first_second_third_lesson_how_many_athletes(self, driver, login):
        lesson_how_many_athletes = FirstSecondThirdLessonHowManyAthletesPage(driver)
        lesson_how_many_athletes.open(UrlsFirstSecondThird.HOW_MANY_ATHLETES)
        lesson_how_many_athletes.drag_cheese_to_basket_cheese()
        lesson_how_many_athletes.drag_bread_to_first_basket_buns()
        lesson_how_many_athletes.drag_salade_to_basket_salade()
        lesson_how_many_athletes.drag_bread_to_first_basket_buns()
        lesson_how_many_athletes.drag_cheese_to_basket_cheese()
        lesson_how_many_athletes.drag_cheese_to_basket_cheese()
        lesson_how_many_athletes.drag_four_chicken_legs_to_basket_by_four()
        lesson_how_many_athletes.drag_three_chicken_legs_to_basket_by_three()
        lesson_how_many_athletes.drag_three_chicken_legs_to_basket_by_three()
        lesson_how_many_athletes.drag_four_chicken_legs_to_basket_by_four()
        lesson_how_many_athletes.drag_order_tea_to_second_tray()
        lesson_how_many_athletes.drag_order_french_fries_to_third_tray()
        lesson_how_many_athletes.drag_order_ice_cream_to_first_tray()
        lesson_how_many_athletes.drag_order_burger_to_second_tray()
        lesson_how_many_athletes.drag_order_cake_to_fourth_tray()
        lesson_how_many_athletes.drag_order_chicken_leg_to_third_tray()
        lesson_how_many_athletes.drag_order_first_bag_to_third_tray()
        lesson_how_many_athletes.drag_order_second_bag_to_first_tray()
        lesson_how_many_athletes.drag_order_third_bag_to_second_tray()
        lesson_how_many_athletes.check_headbar_logo_is_displayed()

    def test_math_first_second_third_lesson_poryadkovye_chislitelnye(self, driver, login):
        lesson_poryadkovye_chislitelnye = FirstSecondThirdLessonPoryadkovyeChislitelnyePage(driver)
        lesson_poryadkovye_chislitelnye.open(UrlsFirstSecondThird.PORYADKOVYE_CHISLITELNYE)
        # lesson_poryadkovye_chislitelnye.click_on_button_key_5_fill_input()
        lesson_poryadkovye_chislitelnye.drag_first_zavrik_on_first_position()
        pass
        #не получается реализовать сортер, нет локаторов у элементов

    def test_math_first_second_third_lesson_who_in_which_carriage(self, driver, login):
        lesson_who_in_which_carriage = FirstSecondThirdLessonWhoInWhichCarriagePage(driver)
        lesson_who_in_which_carriage.open(UrlsFirstSecondThird.WHO_IN_WHICH_CARRIAGE)
        lesson_who_in_which_carriage.click_on_first_carriage()
        lesson_who_in_which_carriage.click_on_fourth_carriage()
        lesson_who_in_which_carriage.drag_animal_in_third_carriage()
        lesson_who_in_which_carriage.drag_animal_in_first_carriage()
        lesson_who_in_which_carriage.drag_animal_in_second_carriage()
        lesson_who_in_which_carriage.drag_animal_in_fourth_carriage()
        lesson_who_in_which_carriage.drag_animal_in_second_carriage()
        lesson_who_in_which_carriage.drag_animal_in_fourth_carriage()
        lesson_who_in_which_carriage.drag_animal_in_third_carriage()
        lesson_who_in_which_carriage.drag_animal_in_first_carriage()
        lesson_who_in_which_carriage.check_headbar_logo_is_displayed()
