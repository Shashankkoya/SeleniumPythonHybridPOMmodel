from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
url="https://www.globalsqa.com/demo-site/datepicker/"
driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']")
time.sleep(2)
frameLo = driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame']")
driver.switch_to.frame(frameLo)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#datepicker").click()
time.sleep(2)

current_date=datetime.now()

next_date=current_date+timedelta(days=1)

formatted_date=next_date.strftime("%m/%d/%Y")

driver.find_element(By.CSS_SELECTOR,"#datepicker").send_keys(formatted_date + Keys.ENTER)
time.sleep(5)
driver.quit()