import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #used to scroll from the page beginning to end
driver.find_element(By.XPATH,'')
time.sleep(5)
checkboxes=driver.find_element(By.XPATH,'//input[@type="checkbox"]')

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
time.sleep(5)
checked_boxes =0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_boxes +=1

assert checked_boxes == 7
time.sleep(5)
print('Checked boxes count is verified')


