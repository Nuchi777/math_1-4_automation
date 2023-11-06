from pages.math_study_lesson_page import MathStudyLessonPage
from pages.math_study_topic_page import MathStudyTopicPage
from pages.main_profile_students_page import MainProfileStudentsPage



class TestMathCosmicAdventureStartPage:

    def test_test(self, driver, login):
        main_profile_students_page = MainProfileStudentsPage(driver)
        main_profile_students_page.click_on_card_math()
        math_study_topic_page = MathStudyTopicPage(driver)
        math_study_topic_page.click_on_cosmic_adventure_lesson()
        math_study_lesson_page = MathStudyLessonPage(driver)
        math_study_lesson_page.click_on_card_start()



