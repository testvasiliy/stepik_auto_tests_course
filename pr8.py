from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math
try: 
    link = "http://suninjuly.github.io/selects1.html"#Переход по ссылке
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1")
    x = int(x.text)
    y = browser.find_element(By.ID, "num2")
    y = int(y.text)
    sum = (int(x)+int(y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(value=str(sum))
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
finally:
    time.sleep(10)
    browser.quit()