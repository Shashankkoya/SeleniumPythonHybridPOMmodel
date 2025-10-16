from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
url="https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
driver.maximize_window()
time.sleep(3)
actions = ActionChains(driver)
hover_element=driver.find_element(By.XPATH,"//a[normalize-space()='SwitchTo']")
time.sleep(2)
actions.move_to_element(hover_element).perform()
driver.find_element(By.CSS_SELECTOR,"a[href='Frames.html']").click()
time.sleep(2)