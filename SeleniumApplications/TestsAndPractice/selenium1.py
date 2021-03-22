from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\MiscProgrammingThings\chromedriver.exe")
driver.get("http://python.org")

assert "Python" in driver.title  ## Check if python is in page title

elem = driver.find_element_by_name("q") ## Get text element

elem.clear() ## Clear text from elements
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source

driver.close()