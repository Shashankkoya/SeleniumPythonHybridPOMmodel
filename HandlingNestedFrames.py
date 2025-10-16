from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/nested_frames')
driver.maximize_window()
time.sleep(3)

# Switching to top frame
driver.switch_to.frame("frame-top")
time.sleep(3)

# Switching to middle frame
driver.switch_to.frame("frame-middle")
time.sleep(3)
content=driver.find_element(By.ID,"content").text
print("content in middle frame:", content)

# Switching to default content
driver.switch_to.default_content()

# Switching to bottom frame
driver.switch_to.frame("frame-bottom")
time.sleep(2)
print("content in bottom frame:", driver.find_element(By.TAG_NAME,"body").text)