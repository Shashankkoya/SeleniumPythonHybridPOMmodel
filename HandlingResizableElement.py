from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
url="https://demo.automationtesting.in/Resizable.html"
driver.get(url)
driver.maximize_window()
time.sleep(3)
actions = ActionChains(driver)
resizable_element = driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
time.sleep(2)
initial_element_size = driver.find_element(By.XPATH,"//div[@id='resizable']")
time.sleep(2)
initial_size = initial_element_size.size
print(initial_size)
actions.click_and_hold(resizable_element).move_by_offset(100,100).release().perform()
time.sleep(2)
resized_size = initial_element_size.size
print(resized_size)
driver.quit()