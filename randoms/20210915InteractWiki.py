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

driver.get("www.website.com/wefsf/wer")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("dez")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("line")
email = driver.find_element_by_name("email")
email.send_keys("dez@dez.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()



