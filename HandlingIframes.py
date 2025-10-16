from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"a[href='/frames']").click()
time.sleep(3)
driver.execute_script("window.scrollTo(0,700)")
driver.find_element(By.XPATH,"//a[normalize-space()='iFrame']").click()
time.sleep(3)
iframe=driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(iframe)
text_editor=driver.find_element(By.XPATH,"//p[normalize-space()='Your content goes here.']")
text_editor.clear()
time.sleep(3)
text_editor.send_keys("This is Selenium with Python Iframe tutorial")
time.sleep(7)
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//a[normalize-space()='Elemental Selenium']").click()
time.sleep(3)
driver.quit()
