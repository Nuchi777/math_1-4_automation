import time

from pages.math.first_second_third_lesson_how_many_athletes_page import FirstSecondThirdLessonHowManyAthletesPage
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

