from selenium import webdriver

chrome_driver_path = "users/kenny/dev/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a")
#print(article_count.text)
article_count.click()

