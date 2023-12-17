from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_FIELD = (By.XPATH, '//input[@id="login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '(//button[@type="submit"])[1]')
    HEADBAR_LOGO = (By.XPATH, '//div[@data-testid="headbar-logo"]')
    TITLE_BASE_COURSE_FINISH = (By.XPATH, '//h3[text()="Поздравляю!"]')
    BUTTON_DECIDE_FURTHER = (By.LINK_TEXT, 'Решать дальше')