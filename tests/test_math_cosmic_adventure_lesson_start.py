import time

from pages.cosmic_adventure_lesson_start_page import CosmicAdventureLessonStartPage
from data import UrlsCosmicAdventure


class TestMathCosmicAdventureStart:

    def test_math_cosmic_adventure_start(self, driver, login):
        lesson_start = CosmicAdventureLessonStartPage(driver)
        lesson_start.open(UrlsCosmicAdventure.START)
        time.sleep(10)












