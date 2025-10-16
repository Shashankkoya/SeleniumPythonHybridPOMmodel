import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/broken_images')
driver.maximize_window()
time.sleep(3)

images = driver.find_elements(By.TAG_NAME, 'img')
broken_images = []
for image in images:
    src = image.get_attribute('src')
    if src:
        response = requests.get(src)
    if response.status_code != 200:
        broken_images.append(src)
        time.sleep(3)
        print("This is a Broken Image")

if broken_images:
    print("These are broken images:")
    for image in broken_images:
        print(image)
else:
    print("No broken images")