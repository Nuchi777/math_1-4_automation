import time

from data import UrlsWhatIsHomeland
from pages.env.what_is_homeland_lesson_homeland_page import WhatIsHomelandLessonHomelandPage
from pages.env.what_is_homeland_lesson_where_animals_live_page import \
    WhatIsHomelandLessonWhereAnimalsLivePage
from pages.env.what_is_homeland_lesson_where_does_person_live_page import \
    WhatIsHomelandLessonWhereDoesPersonLivePage
from pages.env.what_is_homeland_lesson_where_you_live_page import WhatIsHomelandLessonWhereYouLivePage


class TestEnvWhatIsHomeland:

    def test_env_what_is_homeland_lesson_where_animals_live(self, driver, login):
        lesson_where_animals_live = WhatIsHomelandLessonWhereAnimalsLivePage(driver)
        lesson_where_animals_live.open(UrlsWhatIsHomeland.WHERE_ANIMALS_LIVE)
        lesson_where_animals_live.drag_card_fish_in_package_in_river()
        lesson_where_animals_live.drag_card_monkey_in_package_on_three()
        lesson_where_animals_live.drag_card_bird_in_package_in_nest()
        lesson_where_animals_live.check_headbar_logo_is_displayed()

    def test_env_what_is_homeland_lesson_where_does_person_live(self, driver, login):
        lesson_where_does_person_live = WhatIsHomelandLessonWhereDoesPersonLivePage(driver)
        lesson_where_does_person_live.open(UrlsWhatIsHomeland.WHERE_DOES_PERSON_LIVE)
        lesson_where_does_person_live.click_on_homeland_button()
        lesson_where_does_person_live.click_on_russia_button()
        lesson_where_does_person_live.click_on_usa_button()
        lesson_where_does_person_live.click_on_word_homeland()
        lesson_where_does_person_live.check_headbar_logo_is_displayed()

    def test_env_what_is_homeland_lesson_homeland(self, driver, login):
        lesson_homeland = WhatIsHomelandLessonHomelandPage(driver)
        lesson_homeland.open(UrlsWhatIsHomeland.HOMELAND)
        lesson_homeland.click_on_city_card()
        lesson_homeland.click_on_district_card()
        lesson_homeland.click_on_village_card()
        lesson_homeland.click_on_hamlet_card()
        lesson_homeland.click_on_done_button()
        lesson_homeland.click_on_word_city()
        lesson_homeland.click_on_word_district()
        lesson_homeland.click_on_word_village()
        lesson_homeland.click_on_word_hamlet()
        lesson_homeland.click_on_card_i_born_in_village_sukhovo()
        lesson_homeland.click_on_card_i_born_in_omsk()
        lesson_homeland.click_on_word_small_homeland()
        lesson_homeland.click_on_word_homeland()
        lesson_homeland.click_on_word_small_homeland()
        lesson_homeland.click_on_word_homeland()
        lesson_homeland.check_headbar_logo_is_displayed()

    def test_env_what_is_homeland_lesson_where_you_live(self, driver, login):
        lesson_where_you_live = WhatIsHomelandLessonWhereYouLivePage(driver)
        lesson_where_you_live.open(UrlsWhatIsHomeland.WHERE_YOU_LIVE)
        lesson_where_you_live.drag_any_item_to_city_area()
        lesson_where_you_live.click_on_done_button()
        lesson_where_you_live.check_headbar_logo_is_displayed()


