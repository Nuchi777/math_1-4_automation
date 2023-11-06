from selenium.webdriver.common.by import By


class MathStudyLessonPageLocators:

    # МАТЕМАТИКА_КОСМИЧЕСКОЕ_ПРИКЛЮЧЕНИЕ_СТАРТ_КАРТОЧКИ
    CARD_PREVIEW_START = (By.XPATH, '//span[@class="sc-ksBlkl jiNsyf" and text()="Старт"]')
    CARD_PREVIEW_EXPLORE_PLANET = (By.XPATH, "//div[@class='sc-eLQSJh bzuwoY']")
    CARD_PREVIEW_FIX_ROCKET = (By.XPATH, "//div[@class='sc-eLQSJh fDAItz']")
    CARD_PREVIEW_SAVE_KNYSH = (By.XPATH, "//div[@class='sc-eLQSJh gtyclv']")

    PLAY_BUTTON_CARD = (By.XPATH, '//div[@class="play-button play-button_0"]')

