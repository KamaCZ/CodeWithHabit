# Selenium enabales us programatically control the webbrowser firefox
# including logins, submiting etc.
# mac users: sudo -H pip3 install selenium

from selenium import webdriver

browser = webdriver.Firefox()  # calling the webdriver.Firefox() function to launch the webbrowser, it will return the browser object stored in the variable

browser.get("http://kamilklemsa.cz/")

elem = browser.find_element_by_css_selector("#top-menu > li:nth-child(2) > a:nth-child(1)")
print(elem)
elem.click()

elems = browser.find_elements_by_css_selector("p")
print(len(elems))


