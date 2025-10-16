from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = ("admin")
password = ("admin")

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)

# https://username:password@domain_name
