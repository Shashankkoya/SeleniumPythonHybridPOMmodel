from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
time.sleep(3)
driver.get("https://www.google.com/?zx=1760220840471&no_sw_cr=1")
time.sleep(3)