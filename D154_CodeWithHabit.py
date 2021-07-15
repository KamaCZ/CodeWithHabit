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

#driver.back()
#driver.forward()
driver.refresh()
legal.click()