from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url="https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
driver.maximize_window()
time.sleep(3)

alert_button=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
time.sleep(2)
alert=driver.switch_to.alert
alert_text=alert.text
print(alert_text)
time.sleep(2)
alert.accept()
time.sleep(2)

