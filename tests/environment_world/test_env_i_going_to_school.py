import time

from pages.environment_world.i_going_to_school_lesson_daily_regime_schoolkid_page import \
    IGoingToSchoolLessonDailyRegimeSchoolkidPage
from pages.environment_world.i_going_to_school_lesson_day_knowledge_page import IGoingToSchoolLessonDayKnowledgePage
from data import UrlsIGoingToSchool
from pages.environment_world.i_going_to_school_lesson_get_ready_for_school_page import \
    IGoingToSchoolLessonGetReadyForSchoolPage
from pages.environment_world.i_going_to_school_lesson_my_school_page import IGoingToSchoolLessonMySchoolPage


class TestEnvIGoingToSchool:

    def test_env_i_going_to_school_lesson_day_knowledge(self, driver, login):
        lesson_day_knowledge = IGoingToSchoolLessonDayKnowledgePage(driver)
        lesson_day_knowledge.open(UrlsIGoingToSchool.DAY_KNOWLEDGE)
        lesson_day_knowledge.drag_1_january_in_new_year_package()
        lesson_day_knowledge.drag_9_may_in_victory_day_package()
        lesson_day_knowledge.drag_1_september_in_day_of_knowledge_package()
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

    def test_env_i_going_to_school_lesson_my_school(self, driver, login):
        lesson_my_school = IGoingToSchoolLessonMySchoolPage(driver)
        lesson_my_school.open(UrlsIGoingToSchool.MY_SCHOOL)
        lesson_my_school.drag_card_in_classroom_izo_in_draw_package()
        lesson_my_school.drag_card_in_dining_room_in_eating_package()
        lesson_my_school.drag_card_in_library_in_reading_books_package()
        lesson_my_school.drag_card_in_classroom_in_learning_package()
        lesson_my_school.drag_card_in_wardrobe_in_undress_package()
        lesson_my_school.drag_card_in_gym_in_run_package()
        lesson_my_school.drag_card_hustle_in_cannot_package()
        lesson_my_school.drag_card_ride_on_railing_in_cannot_package()
        lesson_my_school.drag_card_help_in_can_package()
        lesson_my_school.drag_card_greet_in_can_package()
        lesson_my_school.drag_card_fight_in_cannot_package()
        lesson_my_school.check_headbar_logo_is_displayed()

    def test_env_i_going_to_school_lesson_daily_regime_schoolkid(self, driver, login):
        lesson_daily_regime_schoolkid = IGoingToSchoolLessonDailyRegimeSchoolkidPage(driver)
        lesson_daily_regime_schoolkid.open(UrlsIGoingToSchool.DAILY_REGIME_SCHOOLKID)
        lesson_daily_regime_schoolkid.click_on_card_with_time_8_00()
        lesson_daily_regime_schoolkid.click_on_card_with_time_8_30()
        lesson_daily_regime_schoolkid.click_on_card_with_time_13_00()
        lesson_daily_regime_schoolkid.click_on_card_with_time_17_00()
        lesson_daily_regime_schoolkid.click_on_card_with_time_21_00()
        lesson_daily_regime_schoolkid.drag_card_wake_up_for_time_7_30()
        lesson_daily_regime_schoolkid.check_headbar_logo_is_displayed()






