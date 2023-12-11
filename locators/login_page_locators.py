from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_FIELD = (By.XPATH, '//input[@id="login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '(//button[@type="submit"])[1]')
    ALL_CARD = (By.XPATH, '//div[@class="sc-jIRcFI iczUfj"]')