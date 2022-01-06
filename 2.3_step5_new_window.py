import time
import math
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    current_window = browser.current_window_handle
    print(current_window)
    browser.find_element_by_class_name("trollface.btn.btn-primary").click()
    second_window = browser.window_handles[1]
    print(second_window)
    browser.switch_to.window(second_window)

    x = browser.find_element_by_id('input_value').text
    y = str(math.log(abs(12*math.sin(int(x)))))

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)
    browser.find_element_by_css_selector("button.btn").click()


finally:
    time.sleep(60)
    browser.quit()
