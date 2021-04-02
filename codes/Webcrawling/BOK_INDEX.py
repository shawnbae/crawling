from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 100대 통계지표 엑셀로 다운로드하기
def download_bok_statistics():
  
  driver = webdriver.Chrome("c:/chromedriver.exe")
  driver.implicitly_wait(3)
  driver.get("http://ecos.bok.or.kr/jsp/vis/keystat/#/key")
  
  excel_download = driver.find_element_by_css_selector('img[alt="download"]')
  driver.implicitly_wait(3)
  
  excel_download.click()
  time.sleep(5)
  
  driver.close()
  print("파일 다운로드 실행 중")
  
  return None

download_bok_statistics()

