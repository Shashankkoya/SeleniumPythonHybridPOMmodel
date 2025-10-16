import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
page_url='https://the-internet.herokuapp.com/dropdown'
driver.get(page_url)
time.sleep(3)

dropdown_element=driver.find_element(By.ID,'dropdown')
select = Select(dropdown_element)
time.sleep(3)
# dropdown_count = len(select.options)
# assert dropdown_count == 3
# print(dropdown_count)
# time.sleep(3)
# select the value by visible text
# select the value by index
# select the option by using value
# select.select_by_index(2)
# select.select_by_value("2")
# select.select_by_visible_text('Option 2')
# time.sleep(3)
target_value = "Option 2"
for dropdown in select.options:
    if dropdown.text == target_value:
        dropdown.click()
        time.sleep(3)
        print(dropdown.text)
        break
