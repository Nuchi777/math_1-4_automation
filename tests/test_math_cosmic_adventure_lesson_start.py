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
        lesson_start.click_on_first_porthole_3_times()
        lesson_start.click_on_second_porthole_3_times()
        lesson_start.click_on_button_with_number_2_step_1()
        lesson_start.click_on_button_with_number_3_step_1()
        lesson_start.click_on_button_with_number_4_step_1()
        lesson_start.click_on_button_with_number_5_step_1()
        lesson_start.click_on_button_with_number_6_step_1()
        lesson_start.click_on_button_with_number_2_step_2()
        lesson_start.click_on_button_with_number_4_step_2()
        lesson_start.click_on_button_with_number_6_step_2()
        lesson_start.click_on_button_with_number_8_step_2()
        lesson_start.click_on_button_with_number_10_step_2()
        lesson_start.click_on_next_button()
        lesson_start.check_table_marathon_is_displayed()
















