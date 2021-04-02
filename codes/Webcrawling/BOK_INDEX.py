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
    driver = webdriver.Chrome("c:/chromedriver.exe")
    driver.implicitly_wait(3)
    driver.get("http://ecos.bok.or.kr/jsp/vis/keystat/#/key")
    time.sleep(5)
    
    items1 = driver.find_elements_by_css_selector('a[class="ng-binding"]')
    items2 = driver.find_elements_by_css_selector('a[class="a-c1-list ng-binding"]')  
    items3 = driver.find_elements_by_css_selector('a[class="a-c4-list ng-binding"]')  
    driver.implicitly_wait(3)
    
    items = items1[1:] + items2 + items3
    
    for idx, item in enumerate(items):
      if keyword in item.text:
        print("검색어 '%s'에 매칭되는 '%s' 통계지표 검색중" % (keyword, item.text))
        item.click()
        item_found = 1
        time.sleep(5)
        break
      elif idx == (len(items) - 1):
        print("검색어 '%s'에 대한 통계지표가 존재하지 않습니다" % keyword)
        driver.close()
        continue
      else:
        pass
      
    # 검색결과 로딩 HTML 웹 페이지를 파싱 - 통계지표 테이블(표) 양식 정리
    html_src = driver.page_source
    soup = BeautifulSoup(html_src, 'html.parser')
    driver.close()
    
    table_items = soup.find_all('td', {'class':'ng-binding'})
    date = [t.text for i, t in enumerate(table_items) if i % 3 == 0]
    value = [t.text for i, t in enumerate(table_items) if i % 3 == 1]
    change = [t.text for i, t in enumerate(table_items) if i % 3 == 2]
    
    # CSV형태의 파일로 저장하기
    result_file = open('../../dataset/bok_statistics_%s.csv' % keyword, 'w')
    
    for i in range(len(date)):
      result_file.write("%s, %s, %s" % (date[i], value[i], change[i]))
      result_file.write('\n')
      
    result_file.close()
    print("키워드 '%s'에 대한 통계지표를 저장하였습니다." % keyword)
    
    return date, value, change
  
# "CD수익률" 통계지표를 별도로 검색, CSV 파일로 저장하기
result = download_bok_statistics_by_keyword()
print(result)