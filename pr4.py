from selenium import webdriver
import time 
link = "http://suninjuly.github.io/registration2.html"#Переход по ссылке
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector('div.first_block > div.form-group.first_class > input') #Имя обязательное поле
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('div.first_block > div.form-group.second_class > input') #Фамилия обязательное поле
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('div.form-group.third_class > input') #Email обязательное поле
    input3.send_keys("mail@gmail.com")
    input4 = browser.find_element_by_css_selector('div.second_block > div.form-group.first_class > input') #Телефон
    input4.send_keys("89000000000")
    input5 = browser.find_element_by_css_selector('div.second_block > div.form-group.second_class > input') #Адрес
    input5.send_keys("ул. Пушкина, д. Колотушкина")
    time.sleep(3)
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(3)
    browser.quit()
