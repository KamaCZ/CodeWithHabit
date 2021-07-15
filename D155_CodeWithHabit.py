# web scraping with selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Applications/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://iba-world.com/")

legal = driver.find_element_by_class_name("age-gate-submit-yes")
legal.click()
time.sleep(10)

driver.back()
time.sleep(5)
driver.forward()
legal = driver.find_element_by_class_name("age-gate-submit-yes")
legal.click()
driver.refresh()
egal = driver.find_element_by_class_name("age-gate-submit-yes")
legal.click()

# I cant get through the permission

