# pyperclip으로 복사 + 붙여넣기 활용하여 로그인 우회하는 방법
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

def naver_login():
  driver = webdriver.Chrome("c:/chromedriver.exe")
  
  url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
  uid = '네이버 아이디'
  upw = '네이버 비밀번호'
  
  driver.get(url)
  time.sleep(2)
  
  tag_id = driver.find_element_by_name('id')
  tag_pw = driver.find_element_by_name('pw')
  
  tag_id.click()
  pyperclip.copy(uid)
  tag_id.send_keys(Keys.CONTROL, 'v')
  time.sleep(1)
  
  tag_pw.click()
  pyperclip.copy(upw)
  tag_pw.send_keys(Keys.CONTROL, 'v')
  time.sleep(1)
  
  login_btn = driver.find_element_by_id('log.login')
  login_btn.click()
  time.sleep(2)
  
  try:
    login_error = driver.find_element_by_css_selector('#err_common > div > p')
    print('로그인 실패 > ', login_error.text)
  except:
    print('로그인 성공')

naver_login()