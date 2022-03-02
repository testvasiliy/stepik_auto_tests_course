from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")#Переход по ссылке
    element1 = browser.find_element_by_name('firstname')
    element1.send_keys("Ivan")
    element2 = browser.find_element_by_name('lastname') 
    element2.send_keys("Ivan")
    element3 = browser.find_element_by_name('e-mail') 
    element3.send_keys("Ivan")
    elements = browser.find_elements_by_css_selector("[type='text']")
    for element in elements:
        element.send_keys("answ")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()


