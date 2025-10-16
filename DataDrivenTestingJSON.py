from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time

json_file='testdatajson.json'

with open(json_file,'r') as file:
    test_data=json.load(file)

for data in test_data['users']:
    chrome_options=Options()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.ID,"user-name").send_keys(data['username'])
    driver.find_element(By.ID,"password").send_keys(data['password'])
    driver.find_element(By.ID,"login-button").click()
    time.sleep(3)
    driver.quit()

