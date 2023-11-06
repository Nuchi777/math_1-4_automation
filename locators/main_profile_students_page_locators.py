from selenium.webdriver.common.by import By


class MainProfileStudentsPageLocators:

    LESSON_CARD_MATH = (By.XPATH, '(//div[@class="sc-cCjUiG gGSAcj"])[1]')
    LESSON_CARD_RUSSIAN_LANGUAGE = (By.XPATH, '(//div[@class="sc-cCjUiG gGSAcj"])[2]')
    LESSON_CARD_ENGLAND_LANGUAGE = (By.XPATH, '(//div[@class="sc-cCjUiG gGSAcj"])[3]')
    LESSON_CARD_SURROUNDING_WORLD = (By.XPATH, '(//div[@class="sc-cCjUiG gGSAcj"])[4]')