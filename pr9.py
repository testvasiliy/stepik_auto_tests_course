from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
link = " http://SunInJuly.github.io/execute_script.html"#Переход по ссылке
try:
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollTo(0, 150)")
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID,"robotsRule")
    option2.click()
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "vasiliytest.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    #button = browser.find_element_by_xpath("//button[@type='submit']")
    #button.click()   
finally:
    time.sleep(10)
    browser.quit()