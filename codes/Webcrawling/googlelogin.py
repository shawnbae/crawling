from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import pyperclip

your_google_id = ''
your_google_password = ''

driver = webdriver.Chrome("c:/chromedriver.exe")
url = "https://accounts.google.com/signin/v2/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys(your_google_password)
driver.find_element_by_css_selector('.VfPpkd-RLmnJb').click()

(
action.send_keys('@gmail.com').pause(2).key_down(Keys.TAB).key_down(Keys.TAB)
.send_keys('제목입니다.').key_down(Keys.TAB)
.send_keys('abcde').key_down(Keys.ENTER)
.key_down(Keys.SHIFT).send_keys('abcde')
.perform()
)

time.sleep(3)
driver.quit()