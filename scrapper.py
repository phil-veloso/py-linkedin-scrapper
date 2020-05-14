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

# locate search form by_name
search_query = driver.find_element_by_name('q')

# send_keys() to simulate the search text key strokes
search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "London"')

# .send_keys() to simulate the return key 
search_query.send_keys(Keys.RETURN)

# locate URL by_class_name
linkedin_urls = driver.find_elements_by_class_name('iUh30')

# variable linkedin_url is equal to the list comprehension 
linkedin_urls = [url.text for url in linkedin_urls]

# to print all elements within our list 
linkedin_urls

driver.get('https:www.google.com')
sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(3)

linkedin_urls = driver.find_elements_by_class_name('iUh30')
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)

driver.quit()

