import time

from pages.cosmic_adventure_lesson_start_page import CosmicAdventureLessonStartPage
from data import UrlsCosmicAdventure


class TestMathCosmicAdventureStart:

    def test_math_cosmic_adventure_start(self, driver, login):
        lesson_start = CosmicAdventureLessonStartPage(driver)
        lesson_start.open(UrlsCosmicAdventure.START)
        lesson_start.click_on_button_start()
        lesson_start.click_on_next_button()
        lesson_start.click_on_button_key_3_fill_input_1()
        lesson_start.click_on_button_key_4_fill_input_2()
        lesson_start.click_on_button_key_5_fill_input_3()
        lesson_start.click_on_button_key_5_fill_input_4()
        lesson_start.click_on_button_key_5_fill_input_5()
        lesson_start.click_on_next_button()
        lesson_start.click_on_button_6_3_8()
        lesson_start.click_on_button_1_5_4()
        lesson_start.click_on_next_button()
        lesson_start.click_on_point_above_stone()
        lesson_start.click_on_point_below_stone()
        lesson_start.click_on_point_between_stone()
        lesson_start.click_on_point_below_triangular_and_above_round_stone()
        lesson_start.click_on_next_button()
        lesson_start.click_on_porthole_3_times()
        lesson_start.click_on_porthole_3_times()














