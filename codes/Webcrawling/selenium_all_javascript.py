from selenium import webdriver

browser = webdriver.Chrome("c:/chromedriver.exe")
browser.maximize_window()
browser.get('https://naver.com')

# 모니터(해상도) 높이인 1080위치로 스크롤 내리기
browser.execute_script("window.scrollTo(0,1080)")

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내리

# 현재 문서 높이를 가져와서 저장하기
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
  # 스크롤 가장 아래로 내리기
  browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  
  # 페이지 로딩 대기
  time.sleep(interval)
  
  # 현재 문서 높이를 가져와서 저장
  curr_height = browser.execute_script("return document.body.scrollHeight")
  if curr_height == prev_height:
    break
  
  prev_height = curr_height
  
browser.quit()