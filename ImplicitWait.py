from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options=Options()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.saucedemo.com/')
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.ID,"user-name").send_keys('standard_user')
driver.find_element(By.ID,"password").send_keys('secret_sauce')
driver.find_element(By.ID,"login-button").click()

driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()

driver.quit()
