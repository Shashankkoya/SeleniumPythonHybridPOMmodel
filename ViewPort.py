import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.google.com/')
time.sleep(5)
driver.set_window_size(1400, 900)
time.sleep(5)