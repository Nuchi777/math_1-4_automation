import time

from data import UrlsSpeechAndLanguage
from pages.rus.speech_and_language_lesson_learning_vocabulary_words_page import \
    SpeechAndLanguageLessonLearningVocabularyWordsPage
from pages.rus.speech_and_language_lesson_native_language_page import \
    SpeechAndLanguageLessonNativeLanguagePage
from pages.rus.speech_and_language_lesson_what_is_speech_page import \
    SpeechAndLanguageLessonWhatIsSpeechPage
from pages.rus.speech_and_language_lesson_what_should_speech_be_like_page import \
    SpeechAndLanguageLessonWhatShouldSpeechBeLikePage
from pages.rus.speech_and_language_lesson_why_is_speech_needed_page import \
    SpeechAndLanguageLessonWhyIsSpeechNeededPage


class TestSpeechAndLanguage:

    def test_rus_speech_and_language_lesson_what_is_speech_page(self, driver, login):
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

    def test_rus_speech_and_language_lesson_why_is_speech_needed_page(self, driver, login):
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

    def test_rus_speech_and_language_lesson_what_should_speech_be_like_page(self, driver, login):
        lesson_what_should_speech_be_like = SpeechAndLanguageLessonWhatShouldSpeechBeLikePage(driver)
        lesson_what_should_speech_be_like.open(UrlsSpeechAndLanguage.WHAT_SHOULD_SPEECH_BE_LIKE)
        lesson_what_should_speech_be_like.click_on_look_how_beautiful_their_puppy()
        lesson_what_should_speech_be_like.click_on_hello_lets_play_chess()
        lesson_what_should_speech_be_like.drag_apple_on_give_me_apple_please()
        lesson_what_should_speech_be_like.drag_candy_on_please_treat_me_to_some_candy()
        lesson_what_should_speech_be_like.drag_flashlight_on_give_me_flashlight()
        lesson_what_should_speech_be_like.drag_mug_on_give_me_mug()
        lesson_what_should_speech_be_like.click_on_button_politely()
        lesson_what_should_speech_be_like.click_on_button_accessibly()
        lesson_what_should_speech_be_like.click_on_button_correctly()
        lesson_what_should_speech_be_like.click_on_button_understandable()
        lesson_what_should_speech_be_like.click_on_button_literate()
        lesson_what_should_speech_be_like.click_on_button_polite()
        lesson_what_should_speech_be_like.check_headbar_logo_is_displayed()

    def test_rus_speech_and_language_lesson_native_language_page(self, driver, login):
        lesson_native_language = SpeechAndLanguageLessonNativeLanguagePage(driver)
        lesson_native_language.open(UrlsSpeechAndLanguage.NATIVE_LANGUAGE)
        lesson_native_language.click_on_first_photo_kalmykia()
        lesson_native_language.click_on_second_photo_chuvashia()
        lesson_native_language.click_on_third_photo_Bashkortostan()
        lesson_native_language.click_on_fourth_photo_yakutia()
        lesson_native_language.click_on_option_kalmyk()
        lesson_native_language.click_on_option_chuvash()
        lesson_native_language.click_on_option_yakut()
        lesson_native_language.click_on_option_bashkir()
        lesson_native_language.click_on_option_native_language()
        lesson_native_language.click_on_option_russian_language()
        lesson_native_language.check_headbar_logo_is_displayed()

    def test_rus_speech_and_language_lesson_learning_vocabulary_words_page(self, driver, login):
        lesson_learning_vocabulary_words = SpeechAndLanguageLessonLearningVocabularyWordsPage(driver)
        lesson_learning_vocabulary_words.open(UrlsSpeechAndLanguage.LEARNING_VOCABULARY_WORDS)
        lesson_learning_vocabulary_words.click_on_first_letter_o()
        lesson_learning_vocabulary_words.click_on_option_gorod()
        lesson_learning_vocabulary_words.click_on_letter_g()
        lesson_learning_vocabulary_words.click_on_letter_o()
        lesson_learning_vocabulary_words.click_on_letter_r()
        lesson_learning_vocabulary_words.click_on_letter_o()
        lesson_learning_vocabulary_words.click_on_letter_d()
        lesson_learning_vocabulary_words.click_on_button_done()
        lesson_learning_vocabulary_words.check_headbar_logo_is_displayed()










