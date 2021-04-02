from selenium import webdriver
import time

# 100대 통계지표 엑셀로 다운로드하기
def download_bok_statistics():
  
  driver = webdriver.Chrome("c:/chromedriver.exe")
  driver.implicitly_wait(3)
  