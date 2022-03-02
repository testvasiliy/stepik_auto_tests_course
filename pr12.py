from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
link = "http://suninjuly.github.io/redirect_accept.html"#Переход по ссылке
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    browser.switch_to.window(browser.window_handles[1])
    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element( By.ID, 'answer')
    input1.send_keys(y)
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click() 
finally:
    time.sleep(10)
    browser.quit()