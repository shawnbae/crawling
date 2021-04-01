from selenium import webdriver

driver = webdriver.Chrome("c:/chromedriver.exe")
driver.implicitly_wait(3) # 3초 기다리기 
driver.get("https://www.danawa.com/")

# 다나와 로그인 버튼 누르기
login =  driver.find_element_by_css_selector('li.my_page_service > a')
print("HTML 요소: ", login)
print("태그 이름: ", login.tag_name)
print("문자열: ", login.text)
print("href 속성: ", login.get_attribute('href'))

login.click()
driver.implicitly_wait(3)

# 로그인하기 
my_id = "내 id"
my_pw = "내 password"

driver.find_element_by_id('danawa-member-login-input-id').send_keys(my_id)
driver.implicitly_wait(2)
driver.find_element_by_name('password').send_keys(my_pw)
driver.implicitly_wait(2)
driver.find_element_by_css_selector('button.btn_login').click()


# 관심목록 가져오기
wishlist = driver.find_element_by_css_selector('li.interest_goods_service > a').click()
driver.implicitly_wait(2)
html_src = driver.page_source
driver.close()
print(html_src[:500])

# 관심상품 목록 HTML페이지를 BeautifulSoup로 파싱하기
from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(html_src, 'html.parser')

wish_table = soup.select('table[class="tbl wish_tbl"]')[0]
wish_items = wish_table.select('tbody tr')

for item in wish_items:
  title = item.find('div', {'class':'tit'}).text
  price = item.find('span', {'class':'price'}).text
  link = item.find('a', href = re.compile('prod.danawa.com/info/')).get('href')
  print(title)
  print(price)
  print(link)

# 브라우저 종료하기  
driver.quit()