import time

from pages.math.cosmic_adventure_lesson_explore_planet_page import CosmicAdventureLessonExplorePlanetPage
from pages.math.cosmic_adventure_lesson_fix_rocket_page import CosmicAdventureLessonFixRocketPage
from pages.math.cosmic_adventure_lesson_save_knysh_page import CosmicAdventureLessonSaveKnyshPage
from pages.math.cosmic_adventure_lesson_start_page import CosmicAdventureLessonStartPage
from data import UrlsCosmicAdventure


class TestMathCosmicAdventure:

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
        lesson_start.check_headbar_logo_is_displayed()


    def test_math_cosmic_adventure_explore_planet(self, driver, login):
        lesson_explore_planet = CosmicAdventureLessonExplorePlanetPage(driver)
        lesson_explore_planet.open(UrlsCosmicAdventure.EXPLORE_PLANET)
        lesson_explore_planet.click_on_button_key_3_fill_input_3()
        lesson_explore_planet.click_on_button_key_2_fill_input_2()
        lesson_explore_planet.click_on_button_key_4_fill_input_4()
        lesson_explore_planet.click_on_number_seven()
        lesson_explore_planet.click_on_number_one()
        lesson_explore_planet.click_on_number_five()
        lesson_explore_planet.click_on_next_button()
        lesson_explore_planet.click_on_cifryts()
        lesson_explore_planet.click_on_button_key_5_fill_input()
        lesson_explore_planet.click_on_pic_block_button_number_3()
        lesson_explore_planet.click_on_pic_block_button_number_4()
        lesson_explore_planet.click_on_next_button()
        lesson_explore_planet.drag_wrapper_heat_to_first_position()
        lesson_explore_planet.drag_wrapper_tail_to_last_position()
        lesson_explore_planet.click_on_done_button()
        lesson_explore_planet.click_on_next_button()
        lesson_explore_planet.check_headbar_logo_is_displayed()

    def test_math_cosmic_adventure_fix_rocket(self, driver, login):
        lesson_fix_rocket = CosmicAdventureLessonFixRocketPage(driver)
        lesson_fix_rocket.open(UrlsCosmicAdventure.FIX_ROCKET)
        lesson_fix_rocket.click_on_button_play()
        lesson_fix_rocket.click_on_next_button()
        lesson_fix_rocket.click_on_box_with_three_stones()
        lesson_fix_rocket.click_on_box_with_one_stone()
        lesson_fix_rocket.click_on_zavrik_with_four_stones()
        lesson_fix_rocket.click_on_zavrik_with_three_stones()
        lesson_fix_rocket.click_on_next_button()
        lesson_fix_rocket.drag_rocket_element_to_rocket()
        lesson_fix_rocket.check_headbar_logo_is_displayed()

    def test_math_cosmic_adventure_save_knysh(self, driver, login):
        lesson_save_knysh = CosmicAdventureLessonSaveKnyshPage(driver)
        lesson_save_knysh.open(UrlsCosmicAdventure.SAVE_KNYSH)
        lesson_save_knysh.click_on_button_play()
        lesson_save_knysh.click_on_next_button()
        lesson_save_knysh.click_on_button_key_6_fill_input_1()
        lesson_save_knysh.click_on_button_key_7_fill_input_2()
        lesson_save_knysh.click_on_button_key_1_and_0_fill_input_3()
        lesson_save_knysh.click_on_next_button()
        lesson_save_knysh.drag_rocket_element_to_rocket()
        lesson_save_knysh.click_on_done_button()
        lesson_save_knysh.click_on_button_continue_to_study()
        lesson_save_knysh.check_headbar_logo_is_displayed()
