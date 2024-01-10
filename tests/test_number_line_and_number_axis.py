from data import UrlsNumberLineAndNumberAxis
from pages.math.number_line_and_number_axis_lesson_acquainted_with_number_axis_page import \
    NumberLineAndNumberAxisLessonAcquaintedWithNumberAxisPage
from pages.math.number_line_and_number_axis_lesson_learning_number_order_page import \
    NumberLineAndNumberAxisLessonLearningNumberOrderPage
from pages.math.number_line_and_number_axis_lesson_what_point_grasshopper_page import \
    NumberLineAndNumberAxisLessonWhatPointGrasshopperPage


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

    def test_math_number_line_and_number_axis_lesson_acquainted_with_number_axis(self, driver, login):
        lesson_acquainted_with_number_axis = NumberLineAndNumberAxisLessonAcquaintedWithNumberAxisPage(driver)
        lesson_acquainted_with_number_axis.open(UrlsNumberLineAndNumberAxis.ACQUAINTED_WITH_NUMBER_AXIS)
        lesson_acquainted_with_number_axis.click_on_button_key_1_fill_input_1()
        lesson_acquainted_with_number_axis.click_on_button_key_2_fill_input_2()
        lesson_acquainted_with_number_axis.click_on_button_key_3_fill_input_3()
        lesson_acquainted_with_number_axis.click_on_button_key_4_fill_input_4()
        lesson_acquainted_with_number_axis.click_on_button_key_5_fill_input_5()
        lesson_acquainted_with_number_axis.click_on_button_key_6_fill_input_6()
        lesson_acquainted_with_number_axis.click_on_button_key_7_fill_input_7()
        lesson_acquainted_with_number_axis.click_on_button_key_8_fill_input_8()
        lesson_acquainted_with_number_axis.click_on_button_key_9_fill_input_9()
        lesson_acquainted_with_number_axis.click_on_button_key_2_fill_input_2()
        lesson_acquainted_with_number_axis.click_on_button_key_3_fill_input_3()
        lesson_acquainted_with_number_axis.click_on_button_key_5_fill_input_5()
        lesson_acquainted_with_number_axis.click_on_button_key_6_fill_input_6()
        lesson_acquainted_with_number_axis.click_on_button_key_8_fill_input_8()
        lesson_acquainted_with_number_axis.click_on_button_key_9_fill_input_9()
        lesson_acquainted_with_number_axis.move_zavrik_to_point_4()
        lesson_acquainted_with_number_axis.move_zavrik_to_point_6()
        lesson_acquainted_with_number_axis.move_zavrik_to_point_8()
        lesson_acquainted_with_number_axis.move_zavrik_to_point_3()
        lesson_acquainted_with_number_axis.move_zavrik_to_point_7()
        lesson_acquainted_with_number_axis.move_zavrik_to_point_5()
        lesson_acquainted_with_number_axis.move_zavrik_to_point_9()
        lesson_acquainted_with_number_axis.check_headbar_logo_is_displayed()

    def test_math_number_line_and_number_axis_lesson_what_point_grasshopper(self, driver, login):
        lesson_what_point_grasshopper = NumberLineAndNumberAxisLessonWhatPointGrasshopperPage(driver)
        lesson_what_point_grasshopper.open(UrlsNumberLineAndNumberAxis.WHAT_POINT_GRASSHOPPER)
        lesson_what_point_grasshopper.click_on_button_key_3()
        lesson_what_point_grasshopper.click_on_button_key_5()
        lesson_what_point_grasshopper.click_on_button_key_4()
        lesson_what_point_grasshopper.click_on_button_key_7()
        lesson_what_point_grasshopper.click_on_button_key_2()
        lesson_what_point_grasshopper.click_on_button_key_6()
        lesson_what_point_grasshopper.click_on_button_key_9()
        lesson_what_point_grasshopper.click_on_button_key_8()
        lesson_what_point_grasshopper.click_on_button_key_1()
        lesson_what_point_grasshopper.check_headbar_logo_is_displayed()















