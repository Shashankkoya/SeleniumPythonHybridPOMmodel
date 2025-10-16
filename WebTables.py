import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollTo(0,700)")
time.sleep(2)
table=driver.find_element(By.ID, "countries")
time.sleep(5)
rows=table.find_elements(By.TAG_NAME, "tr")
rows_count=len(rows)
print(rows_count)
target_value = 'Australia'
found=False
for row in rows:
    cells=row.find_elements(By.TAG_NAME,"td")
    for cell in cells:
        if target_value==cell.text:
            found=True
            print("Target value found: ",cell.text)
            break
    if found==True:
        break
else:
    print("Target value not found")
time.sleep(2)
driver.quit()