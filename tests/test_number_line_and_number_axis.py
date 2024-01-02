from data import UrlsNumberLineAndNumberAxis
from pages.math.number_line_and_number_axis_lesson_learning_number_order_page import \
    NumberLineAndNumberAxisLessonLearningNumberOrderPage


class TestNumberLineAndNumberAxis:

    def test_math_number_line_and_number_axis_lesson_learning_number_order(self, driver, login):
        lesson_learning_number_order = NumberLineAndNumberAxisLessonLearningNumberOrderPage(driver)
        lesson_learning_number_order.open(UrlsNumberLineAndNumberAxis.LEARNING_NUMBER_ORDER)
        lesson_learning_number_order.click_on_button_key_1_fill_input_1()
        lesson_learning_number_order.click_on_button_key_7_fill_input_7()
        lesson_learning_number_order.click_on_button_key_3_fill_input_3()
        lesson_learning_number_order.click_on_button_key_9_fill_input_9()
        lesson_learning_number_order.click_on_button_key_2_fill_input_2()
        lesson_learning_number_order.click_on_button_key_6_fill_input_6()
        lesson_learning_number_order.click_on_button_key_2_fill_input_2()
        lesson_learning_number_order.click_on_button_key_3_fill_input_3()
        lesson_learning_number_order.click_on_button_key_7_fill_input_7()
        lesson_learning_number_order.click_on_button_key_8_fill_input_8()
        lesson_learning_number_order.click_on_button_key_5_fill_input_5()
        lesson_learning_number_order.click_on_button_key_6_fill_input_6()
        lesson_learning_number_order.click_on_button_key_5_fill_input_5()
        lesson_learning_number_order.click_on_button_key_7_fill_input_7()
        lesson_learning_number_order.click_on_button_key_9_fill_input_9()
        lesson_learning_number_order.click_on_button_key_4_fill_input_4()
        lesson_learning_number_order.click_on_button_key_6_fill_input_6()
        lesson_learning_number_order.click_on_button_key_9_fill_input_9()
        lesson_learning_number_order.click_on_button_key_1_fill_input_1()
        lesson_learning_number_order.click_on_button_key_3_fill_input_3()
        lesson_learning_number_order.click_on_button_key_8_fill_input_8()
        lesson_learning_number_order.check_headbar_logo_is_displayed()












