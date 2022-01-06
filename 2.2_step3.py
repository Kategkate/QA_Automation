import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/selects1.html")

    x = int(browser.find_element_by_id('num1').get_attribute('num1'))
    y = int(browser.find_element_by_id('num2').get_attribute('num2'))
    summary = x + y

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value("value==summary")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
    print("Тест успешно завершен. 10 сек на закрытие браузера...")

finally:
    time.sleep(10)
    browser.quit()