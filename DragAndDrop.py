from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
url="https://the-internet.herokuapp.com/drag_and_drop"
driver.get(url)
driver.maximize_window()
time.sleep(3)
actions = ActionChains(driver)
source=driver.find_element(By.ID,"column-a")
destination=driver.find_element(By.ID,"column-b")
actions.drag_and_drop(source,destination).perform()
time.sleep(2)