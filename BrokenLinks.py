import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://jqueryui.com/'
driver.get(url)
driver.maximize_window()
time.sleep(3)

all_links = driver.find_elements(By.TAG_NAME, 'a')
time.sleep(3)
print(len(all_links))

for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken Link: {href}, Status Code: {response.status_code}")
driver.quit()
