from selenium import webdriver

# 화면크기 100%로 설정할 것!
# 인터넷 옵션에서 보호모드 사용 끄기
driver = webdriver.Ie("c:/IEDriverServer.exe")
driver.get("https://naver.com")

# 

# from collections import Iterable
# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoAlertPresentException, TimeoutException, UnexpectedAlertPresentException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


# class IEBrowser:
#     def __init__(self):
#         self.driver = webdriver.Ie('./IEDriverServer_2.53.1_x64.exe')  # FIXME: Fixed Driver Path
    
#     def visit(self, url):
#         self.driver.get(url)
#         return self

#     def click(self, element_id):
#         self.driver.find_element_by_id(element_id).click()
#         return self

#     def wait(self, element_id, timeout):
#         expected = EC.presence_of_element_located((By.ID, element_id))
#         WebDriverWait(self.driver, timeout).until(expected)
#         return self

#     def switch_to_frame(self, frame_id):
#         self.driver.switch_to_frame(frame_id)
#         return self
    
#     def alert_dismiss(self):
#         try:
#             self.driver.switch_to_alert().dismiss()
#         except NoAlertPresentException as e:
#             print(e)
#         return self

#     def quit(self):
#         self.driver.quit()
#         return self


# def main():
#     browser = IEBrowser()
#     browser.visit("https://www.hometax.go.kr")

#     try:
#         print("waiting group1300 ...")
#         browser.wait('group1300', 5)

#         print("click group_1300")
#         browser.click('group1300')

#         try:
#             browser.wait('txppIframe', 3)
#         except UnexpectedAlertPresentException as e:
#             print(e)
#             browser.alert_dismiss().alert_dismiss()

#         browser.switch_to_frame('txppIframe').click('a_0111060000')

#         print("3초 뒤에 브라우저를 닫습니다.")
#         time.sleep(3)
#     finally:
#         browser.quit()


# if __name__ == '__main__':
#     main()