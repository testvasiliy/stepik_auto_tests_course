from selenium import webdriver
import time
import math
driver = webdriver.Chrome()
time.sleep(1)
driver.get('http://suninjuly.github.io/find_link_text')
link = driver.find_element_by_link_text('224592').click()
try:
 element1 = driver.find_element_by_name('first_name')
 element1.send_keys("Ivan")
 element2 = driver.find_element_by_name('last_name')
 element2.send_keys("Petrov")
 element3 = driver.find_element_by_name('firstname')
 element3.send_keys("Smolensk")
 element4 = driver.find_element_by_id('country')
 element4.send_keys("Russia")
 button = driver.find_element_by_class_name("btn.btn-default")
 button.click()
finally:
    time.sleep(30)
    browser.quit()
