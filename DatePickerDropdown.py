from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
url="https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
driver.maximize_window()
time.sleep(3)

driver.find_element(By.ID,"datepicker2").click()
time.sleep(2)

current_date=datetime.now()
next_date=current_date+timedelta(days=1)
formated_date=next_date.strftime("%m/%d/%Y")
print(next_date)
Current_day=(str(current_date.day))
print(Current_day)
current_month=datetime.now().month
current_year=datetime.now().year

next_month=(current_month%12)+1
next_month_year=f"{current_month}/{current_year}"
Month_Dropdown = driver.find_element(By.CSS_SELECTOR,"select[title='Change the month']")
select=Select(Month_Dropdown)
select.select_by_value(str(next_month_year))
time.sleep(5)
Year_Dropdown=driver.find_element(By.CSS_SELECTOR,"select[title='Change the year']")
select=Select(Year_Dropdown)
time.sleep(5)
select.select_by_visible_text("2025")
time.sleep(3)
driver.find_element(By.LINK_TEXT,Current_day).click()
time.sleep(5)