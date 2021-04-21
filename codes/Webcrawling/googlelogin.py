from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

your_google_id = ''
your_google_password = ''

driver = webdriver.Chrome("c:/chromedriver.exe")
url = "https://google.com"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_css_selector('.link_login').click()
action.send_keys(your_naver_id).key_down(Keys.TAB).send_keys(your_naver_password).perform()
action.reset_actions()

driver.find_element_by_css_selector('.btn_global').click()



# driver.find_element_by_class_name('gb_g').click()

# time.sleep(3)
# driver.quit()