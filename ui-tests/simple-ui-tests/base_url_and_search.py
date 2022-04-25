from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.get("http://google.com")
browser.find_element(by=By.NAME, value="q").send_keys("test")
browser.find_element(by=By.NAME, value="q").submit()
wait = WebDriverWait(driver=browser, timeout=10)
wait.until(EC.title_is("test - Поиск в Google"))
browser.quit()
