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

# 통계지표 검색어로 CSV파일 저장하기
def download_bok_statistics_by_keyword():
  
  item_found = 0
  while not item_found:
    
    # 검색어 초기화하기
    keyword = ""
    while len(keyword)== 0:
      keyword = str(input("검색할 항목을 입력하세요: "))
      
    # 웹드라이버 실행
    
      
      
      
      