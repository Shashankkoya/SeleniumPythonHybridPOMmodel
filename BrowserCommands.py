import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get('http://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
time.sleep(10)
driver.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(7)
driver.back()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.quit()


