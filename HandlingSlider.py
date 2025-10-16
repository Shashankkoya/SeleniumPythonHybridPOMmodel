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

slider=driver.find_element(By.XPATH,"//input[@type='range']")
actions.click_and_hold(slider).move_by_offset(50,0).release().perform()
time.sleep(2)
driver.quit()