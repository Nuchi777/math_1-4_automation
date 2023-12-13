from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def element_is_visible(self, locator):
        self.scroll_to_element(self.element_is_presence(locator))
        return WebDriverWait(self.driver, timeout=60).until(EC.visibility_of_element_located(locator))

    def element_is_presence(self, locator):
        return WebDriverWait(self.driver, timeout=60).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator):
        return WebDriverWait(self.driver, timeout=60).until(EC.element_to_be_clickable(locator))

    def drag_and_drop_on_to_element(self, draggable_locator, droppable_locator):
        draggable = self.element_is_visible(draggable_locator)
        droppable = self.element_is_visible(droppable_locator)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

    def scroll_to_element(self, locator):
        ActionChains(self.driver).scroll_to_element(locator).perform()

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_window(self, index_page):
        self.driver.switch_to.window(self.driver.window_handles[index_page])

    def element_is_selected(self, locator):
        return WebDriverWait(self.driver, timeout=60).until(EC.element_located_to_be_selected(locator))

    def get_current_title(self):
        WebDriverWait(self.driver, timeout=60).until(EC.visibility_of_element_located(MainPageLocators.MAIN_BANNER))
        return self.driver.title()







