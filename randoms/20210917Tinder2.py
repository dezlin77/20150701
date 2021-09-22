from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import selenium


url = 'https://tinder.com'
path = YOUR_WEB_DRIVER_PATH
email = YOUR EMAIL
password = YOUR EMAIL

driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()
driver.get(url=url)

# login button
login_button = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span')
login_button.click()
sleep(5)

####################### GOOGLE SIGN UP #######################
# buttons
facebook_button = driver.find_element_by_xpath('//*[@id="t-1483503441"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_button.click()

# switching to sign up window.
google_sign_up_window = driver.window_handles[1]
driver.switch_to.window(google_sign_up_window)

# signing up
email_input = driver.find_element_by_id('email')
password_input = driver.find_element_by_id('pass')

email_input.send_keys(email)


password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

# switching back to base window :)
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)

####################### AUTOMATING #######################
# accept cookies
accept_button = driver.find_element_by_xpath('//*[@id="t--771258051"]/div/div[2]/div/div/div[1]/button')
accept_button.click()

# clicking on recommended buttons
sleep(7)
allow_button = driver.find_element_by_xpath('//*[@id="t-1483503441"]/div/div/div/div/div[3]/button[1]')
allow_button.click()

sleep(7)
enable_button = driver.find_element_by_xpath('//*[@id="t-1483503441"]/div/div/div/div/div[3]/button[1]')
enable_button.click()

# rating
dislike_button = driver.find_element_by_xpath(
    '//*[@id="t--771258051"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
like_button = driver.find_element_by_xpath(
    '//*[@id="t--771258051"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')

while True:
    sleep(2)
    try:
        dislike_button.click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        try:
            sleep(1)
            interested_button = driver.find_element_by_xpath('//*[@id="t-1483503441"]/div/div/div[2]/button[1]')
            interested_button.click()
        except selenium.common.exceptions.NoSuchElementException:
            continue


