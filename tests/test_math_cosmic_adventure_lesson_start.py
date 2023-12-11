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













