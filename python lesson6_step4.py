from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name(".form-control.first[placeholder=Input your first name]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_tag_name(".form-control.second[placeholder=Input your last name]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(".form-control.third")
    input3.send_keys("kkk@gmail.com")

    button = browser.find_element_by_css_selector("btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла"
