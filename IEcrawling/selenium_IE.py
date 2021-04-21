from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 인터넷 익스플로러 설정. 아래 사항만 지키면 따로 설정할 필요 없을듯.
# cap = DesiredCapabilities().INTERNETEXPLORER
# cap['ignoreProtectedModeSettings'] = True
# cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
# cap['nativeEvents'] = True
# cap['ignoreZoomSetting'] = True
# cap['requireWindowFocus'] = True
# cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True

# 화면크기 100%로 설정할 것!
# 인터넷 옵션에서 보호모드 사용 끄기
# 모든 설정에 대해 보호모드 사용 꺼야함.
driver = webdriver.Ie("c:/IEDriverServer.exe", capabilities=cap)
driver.get("https://naver.com")
