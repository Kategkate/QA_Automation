from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'
browser.get(link)

try:
    x_element = int(browser.find_element_by_id("num1").text)
    y_element = int(browser.find_element_by_id("num2").text)
    num_value = str(x_element + y_element)
    print(num_value)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(num_value))

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
