


class TestMathCosmicAdventureStart:

    def test_math_cosmic_adventure_start_card_1(self, driver, login):
        main_profile_students_page = MainProfileStudentsPage(driver)
        main_profile_students_page.click_on_card_math()
        math_study_topic_page = MathStudyTopicPage(driver)
        math_study_topic_page.click_on_cosmic_adventure_lesson()
        math_study_lesson_page = MathStudyLessonPage(driver)
        math_study_lesson_page.click_on_card_start()
        lesson_math_cosmic_adventure_start_page = LessonMathCosmicAdventureStartPage(driver)
        lesson_math_cosmic_adventure_start_page.click_on_play_button()
        lesson_math_cosmic_adventure_start_page.click_on_start_button()
        lesson_math_cosmic_adventure_start_page.click_on_next_button()
        lesson_math_cosmic_adventure_start_page.click_on_next_button()
        lesson_math_cosmic_adventure_start_page.input_value(3)








