from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time
link = "http://suninjuly.github.io/file_input.html"#Переход по ссылке
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'firstname') 
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, 'email') 
    input3.send_keys("mail@gmail.com")
    file = browser.find_element_by_css_selector("#file")
    directory = "/Users/alladrozd/"
    file_name = "vasiliytest.txt"
    file_path = os.path.join(directory, file_name)
    file.send_keys(file_path)
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click() 
    time.sleep(3)
finally:
    time.sleep(10)
    browser.quit()