# 
import config

# import web driver
from selenium import webdriver


# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(config.CHROMEDRIVER_PATH)

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login')

# locate email form by_class_name
username = driver.find_element_by_class_name('login-email')

# send_keys() to simulate key strokes
username.send_keys(config.LINKEDIN_USERNAME)

# locate password form by_class_name
password = driver.find_element_by_class_name('login-password')

# send_keys() to simulate key strokes
password.send_keys(config.LINKEDIN_PASSWORD)

# minic human interact
sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()