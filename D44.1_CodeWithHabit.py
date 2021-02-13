# Selenium enabales us programatically control the webbrowser firefox
# including logins, submiting etc.
# mac users: sudo -H pip3 install selenium

from selenium import webdriver

browser = webdriver.Firefox()  # calling the webdriver.Firefox() function to launch the webbrowser, it will return the browser object stored in the variable

browser.get("https://nostarch.com")

elem = browser.find_element_by_css_selector("#hp-app > div > div.drag-and-drop > div.main-content > div > div > div.main-content__content > header > div > div > div.search > ul > li.search__tab.search__tab--zbozi > button > span.tab-button__title-inactive")
print(elem)
elem.click()

elems = browser.find_elements_by_css_selector("p")
print(len(elems))


search_elem = browser.find_element_by_css_selector("#edit-search-block-form--2")
print(search_elem)
# search_elem.send_keys("automatetheboringstuff")
# search_elem.submit()

# check the error message

