from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_FIELD = (By.XPATH, '//input[@id="login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '(//button[@type="submit"])[1]')
    MAIN_BANNER = (By.XPATH, '//div[@class="sc-eDWCr kwxVjR"]')