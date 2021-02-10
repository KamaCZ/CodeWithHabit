from selenium import webdriver


browser = webdriver.Firefox()

browser.get("https://www.amazon.com")

search_elem = browser.find_element_by_css_selector("#twotabsearchtextbox")
print(search_elem)

search_elem.send_keys("fitness")
search_elem.submit()








