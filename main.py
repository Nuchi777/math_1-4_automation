from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

WebDriverWait(driver, timeout=5).until(EC.element_to_be_clickable()
