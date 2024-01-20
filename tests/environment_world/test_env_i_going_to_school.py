import time

from pages.environment_world.i_going_to_school_lesson_day_knowledge_page import IGoingToSchoolLessonDayKnowledgePage
from data import UrlsIGoingToSchool


class TestMathCosmicAdventure:

    def test_env_i_going_to_school_lesson_day_knowledge(self, driver, login):
        lesson_day_knowledge = IGoingToSchoolLessonDayKnowledgePage(driver)
        lesson_day_knowledge.open(UrlsIGoingToSchool.DAY_KNOWLEDGE)
        lesson_day_knowledge.drag_1_january_in_third_package()
        lesson_day_knowledge.drag_9_may_in_first_package()
        lesson_day_knowledge.drag_1_september_in_first_package()
        lesson_day_knowledge.click_on_card_sitting_at_the_desk()
        lesson_day_knowledge.click_on_card_collects_briefcase()
        lesson_day_knowledge.click_on_done_button()
        lesson_day_knowledge.check_headbar_logo_is_displayed()

