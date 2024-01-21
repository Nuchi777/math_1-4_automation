from data import UrlsWhatIsHomeland
from pages.environment_world.what_is_homeland_lesson_where_animals_live_page import \
    WhatIsHomelandLessonWhereAnimalsLivePage


class TestWhatIsHomeland:

    def test_env_what_is_homeland_lesson_where_animals_live(self, driver, login):
        lesson_where_animals_live = WhatIsHomelandLessonWhereAnimalsLivePage(driver)
        lesson_where_animals_live.open(UrlsWhatIsHomeland.WHERE_ANIMALS_LIVE)
        lesson_where_animals_live.drag_card_fish_in_package_in_river()
        lesson_where_animals_live.drag_card_monkey_in_package_on_three()
        lesson_where_animals_live.drag_card_bird_in_package_in_nest()
        lesson_where_animals_live.check_headbar_logo_is_displayed()
