import math
import time
from selenium import webdriver

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x = browser.find_element_by_id('treasure').get_attribute("valuex")
    y = str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()