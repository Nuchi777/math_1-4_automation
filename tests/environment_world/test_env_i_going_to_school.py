import time
from pages.environment_world.i_going_to_school_lesson_day_knowledge_page import IGoingToSchoolLessonDayKnowledgePage
from data import UrlsIGoingToSchool
from pages.environment_world.i_going_to_school_lesson_get_ready_for_school_page import \
    IGoingToSchoolLessonGetReadyForSchoolPage


class TestEnvIGoingToSchool:

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

    def test_env_i_going_to_school_lesson_get_ready_for_school(self, driver, login):
        lesson_get_ready_for_school = IGoingToSchoolLessonGetReadyForSchoolPage(driver)
        lesson_get_ready_for_school.open(UrlsIGoingToSchool.GET_READY_FOR_SCHOOL)
        lesson_get_ready_for_school.drag_kite_in_leave_at_home_bag()
        lesson_get_ready_for_school.drag_book_in_take_to_school_bag()
        lesson_get_ready_for_school.drag_pencil_case_in_take_to_school_bag()
        lesson_get_ready_for_school.drag_ice_cream_in_leave_at_home_bag()
        lesson_get_ready_for_school.drag_notebook_in_take_to_school_bag()
        lesson_get_ready_for_school.click_on_ice_cream()
        lesson_get_ready_for_school.click_on_sled()
        lesson_get_ready_for_school.click_on_cat()
        lesson_get_ready_for_school.check_headbar_logo_is_displayed()


