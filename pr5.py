from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input') #Имя обязательное поле
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input') #Фамилия обязательное поле
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'div.form-group.third_class > input') #Email обязательное поле
    input3.send_keys("mail@gmail.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
