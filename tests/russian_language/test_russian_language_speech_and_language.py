import time

from data import UrlsSpeechAndLanguage

from pages.russian_language.speech_and_language_lesson_what_is_speech_page import \
    SpeechAndLanguageLessonWhatIsSpeechPage


class TestSpeechAndLanguage:

    def test_russian_language_speech_and_language_lesson_what_is_speech_page(self, driver, login):
        what_is_speech_page = SpeechAndLanguageLessonWhatIsSpeechPage(driver)
        what_is_speech_page.open(UrlsSpeechAndLanguage.WHAT_IS_SPEECH)
        what_is_speech_page.drag_cat_in_package_meows()
        what_is_speech_page.drag_human_in_package_speaks()
        what_is_speech_page.drag_dog_in_package_barks()
        what_is_speech_page.drag_mewing_in_package_with_cat()
        what_is_speech_page.drag_speech_in_package_with_human()
        what_is_speech_page.drag_bark_in_package_with_dog()
        what_is_speech_page.click_on_button_speak()
        what_is_speech_page.click_on_button_humans()
        what_is_speech_page.check_headbar_logo_is_displayed()

