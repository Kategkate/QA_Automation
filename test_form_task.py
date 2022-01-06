import time
from selenium import webdriver

browser = webdriver.Chrome()
link = 'https://arturmkr.github.io/simple_web_site/form.html'

try:
    browser.get(link)
    bike_vehicle = browser.find_element_by_id("vehicle1").is_selected()
    print("I have a bike - ", bike_vehicle)

    car_vehicle = browser.find_element_by_id("vehicle2").get_attribute("disabled")
    if car_vehicle is not None:
        print("I have a car disabled - ", car_vehicle)
    else:
        print("I have a car enabled - false")

    boat_vehicle = browser.find_element_by_id("vehicle3").is_selected()
    print("Checkbox is not checked, all is fine")

    language = browser.find_element_by_id("css").is_selected()
    print("CSS language is checked, all is fine")

finally:
    time.sleep(5)
    browser.quit()
