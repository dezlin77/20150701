from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "users/kenny/dev/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a")
#print(article_count.text)
#article_count.click()

all_portals = find_element_by_link_text("all portals")
#all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


=====================



