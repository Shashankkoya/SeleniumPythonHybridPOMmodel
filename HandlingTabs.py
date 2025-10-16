import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.maximize_window()
time.sleep(5)
driver.switch_to.new_window()
driver.get("https://playwright.dev/")
time.sleep(5)
len_of_tabs = len(driver.window_handles)
print(len_of_tabs)
tabs_value=driver.window_handles
print(tabs_value)
current_tab=driver.current_window_handle
print(current_tab)
driver.find_element(By.CSS_SELECTOR,'.getStarted_Sjon').click()
time.sleep(5)
first_tab=driver.window_handles[0]
if current_tab!=first_tab:
    driver.switch_to.window(first_tab)
driver.find_element(By.XPATH,'//span[normalize-space()="Downloads"]').click()
time.sleep(5)

driver.quit()