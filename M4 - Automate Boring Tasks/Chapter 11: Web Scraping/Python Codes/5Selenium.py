from selenium import webdriver
from selenium.webdriver.common.keys import keys
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)	# scrolls to bottom
htmlElem.send_keys(Keys.HOME)	# scrolss to top