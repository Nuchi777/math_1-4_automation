import time

from data import UrlsSpeechAndLanguage

from pages.russian_language.speech_and_language_lesson_what_is_speech_page import \
    SpeechAndLanguageLessonWhatIsSpeechPage
from pages.russian_language.speech_and_language_lesson_why_is_speech_needed_page import \
    SpeechAndLanguageLessonWhyIsSpeechNeededPage


class TestSpeechAndLanguage:

    def test_russian_language_speech_and_language_lesson_what_is_speech_page(self, driver, login):
        lesson_what_is_speech = SpeechAndLanguageLessonWhatIsSpeechPage(driver)
        lesson_what_is_speech.open(UrlsSpeechAndLanguage.WHAT_IS_SPEECH)
        lesson_what_is_speech.drag_cat_in_package_meows()
        lesson_what_is_speech.drag_human_in_package_speaks()
        lesson_what_is_speech.drag_dog_in_package_barks()
        lesson_what_is_speech.drag_mewing_in_package_with_cat()
        lesson_what_is_speech.drag_speech_in_package_with_human()
        lesson_what_is_speech.drag_bark_in_package_with_dog()
        lesson_what_is_speech.click_on_button_speak()
        lesson_what_is_speech.click_on_button_humans()
        lesson_what_is_speech.check_headbar_logo_is_displayed()

    def test_russian_language_speech_and_language_lesson_why_is_speech_needed_page(self, driver, login):
        lesson_why_is_speech_needed = SpeechAndLanguageLessonWhyIsSpeechNeededPage(driver)
        lesson_why_is_speech_needed.open(UrlsSpeechAndLanguage.WHY_IS_SPEECH_NEEDED)
        lesson_why_is_speech_needed.click_on_button_question()
        lesson_why_is_speech_needed.click_on_button_tell()
        lesson_why_is_speech_needed.click_on_button_ask()
        lesson_why_is_speech_needed.click_on_button_question()
        lesson_why_is_speech_needed.click_on_button_tell()
        lesson_why_is_speech_needed.click_on_button_ask()
        lesson_why_is_speech_needed.click_on_first_card()
        lesson_why_is_speech_needed.click_on_third_card()
        lesson_why_is_speech_needed.click_on_second_card()
        lesson_why_is_speech_needed.check_headbar_logo_is_displayed()





