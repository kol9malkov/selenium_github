"""
Replacing the user agent
Automatic authorization to the github site,
transition to the profile and a screenshot of the profile in .png
"""

from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
from password import login, password

# create new useragent
useragent = UserAgent(verify_ssl=False)

# options for Firefox
options = webdriver.FirefoxOptions()

# change useragent
options.set_preference("general.useragent.override", useragent.random)


# the path to the Firefox driver
driver = webdriver.Firefox(
    executable_path='Absolute_path_to_the_driver',
    options=options
)

# authorization process
try:
    driver.get(
        url='https://github.com/'
    )
    time.sleep(4)

    sign_click = driver.find_element_by_link_text('Sign in').click()
    time.sleep(2)
    login_input = driver.find_element_by_id('login_field')
    login_input.clear()
    login_input.send_keys(login)
    time.sleep(2)
    password_input = driver.find_element_by_id('password')
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(2)
    sign_in = driver.find_element_by_name('commit').click()
    time.sleep(2)
    to_profile = driver.find_element_by_xpath(
        '/html/body/div[1]/header/div[7]/details/summary'
    )
    to_profile.click()
    time.sleep(2)
    profile = driver.find_element_by_link_text('Your profile').click()
    time.sleep(2)
    driver.save_screenshot('*.png')
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
