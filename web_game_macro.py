import time
from selenium import webdriver

# Chrome WebDriver를 이용해 Chrome을 실행합니다.
driver = webdriver.Chrome('C:/Users/Domangja/AppData/Local/Programs/Python/chromedriver.exe')

# www.google.com으로 이동합니다.
driver.get("https://hentaiverse.org/")
time.sleep(2)