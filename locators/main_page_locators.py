from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_FIELD = (By.XPATH, '//input[@id="login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '(//button[@type="submit"])[1]')
    HEADBAR_LOGO = (By.XPATH, '//div[@data-testid="headbar-logo"]')
    TABLE_MARATHON = (By.XPATH, '//div[@class="elements__Table-marathon__sc-kzzx8a-3 cRzQiC"]')