from pages.math.counting_objects_lesson_take_kitten_to_bus_stop_page import CountingObjectsLessonTakeKittenToBusStopPage
from data import UrlsCountingObjects


class TestMathCountingObjects:

    def test_math_counting_objects_lesson_take_kitten_to_bus_stop(self, driver, login):
        lesson_take_kitten_to_bus_stop = CountingObjectsLessonTakeKittenToBusStopPage(driver)
        lesson_take_kitten_to_bus_stop.open(UrlsCountingObjects.TAKE_KITTEN_TO_BUS_STOP)
