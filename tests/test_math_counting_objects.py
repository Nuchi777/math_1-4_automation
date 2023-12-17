import time

from pages.math.counting_objects_lesson_take_kitten_to_bus_stop_page import CountingObjectsLessonTakeKittenToBusStopPage
from data import UrlsCountingObjects


class TestMathCountingObjects:

    def test_math_counting_objects_lesson_take_kitten_to_bus_stop(self, driver, login):
        lesson_take_kitten_to_bus_stop = CountingObjectsLessonTakeKittenToBusStopPage(driver)
        lesson_take_kitten_to_bus_stop.open(UrlsCountingObjects.TAKE_KITTEN_TO_BUS_STOP)
        lesson_take_kitten_to_bus_stop.click_on_button_key_1_fill_input_1()
        lesson_take_kitten_to_bus_stop.click_on_button_key_2_fill_input_2()
        lesson_take_kitten_to_bus_stop.click_on_button_key_3_fill_input_3()
        lesson_take_kitten_to_bus_stop.click_on_button_key_4_fill_input_4()
        lesson_take_kitten_to_bus_stop.click_on_button_key_5_fill_input_5()
        lesson_take_kitten_to_bus_stop.click_on_button_key_6_fill_input_6()
        lesson_take_kitten_to_bus_stop.click_on_button_key_7_fill_input_7()
        lesson_take_kitten_to_bus_stop.click_on_button_key_8_fill_input_8()
        lesson_take_kitten_to_bus_stop.click_on_button_key_1_fill_input_1()
        lesson_take_kitten_to_bus_stop.click_on_button_key_2_fill_input_2()
        lesson_take_kitten_to_bus_stop.click_on_button_key_3_fill_input_3()
        lesson_take_kitten_to_bus_stop.click_on_button_key_4_fill_input_4()
        lesson_take_kitten_to_bus_stop.click_on_button_key_5_fill_input_5()
        lesson_take_kitten_to_bus_stop.click_on_button_key_1_fill_input_1()
        lesson_take_kitten_to_bus_stop.click_on_button_key_2_fill_input_2()
        lesson_take_kitten_to_bus_stop.click_on_button_key_3_fill_input_3()
        lesson_take_kitten_to_bus_stop.click_on_button_key_4_fill_input_4()
        lesson_take_kitten_to_bus_stop.click_on_button_key_5_fill_input_5()
        lesson_take_kitten_to_bus_stop.click_on_button_key_6_fill_input_6()
        lesson_take_kitten_to_bus_stop.click_on_button_key_7_fill_input_7()
        lesson_take_kitten_to_bus_stop.click_on_house_4()
        lesson_take_kitten_to_bus_stop.click_on_house_2()
        lesson_take_kitten_to_bus_stop.click_on_house_6()
        lesson_take_kitten_to_bus_stop.click_on_house_5()
        lesson_take_kitten_to_bus_stop.click_on_house_3()
        lesson_take_kitten_to_bus_stop.click_on_house_7()
        lesson_take_kitten_to_bus_stop.click_on_house_1()
        lesson_take_kitten_to_bus_stop.check_table_marathon_is_displayed()



