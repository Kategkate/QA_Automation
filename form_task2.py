import time
from selenium import webdriver


def test_check_bike_vehicle():
    browser = webdriver.Chrome()
    link = 'https://arturmkr.github.io/simple_web_site/form.html'

    try:
        browser.get(link)
        bike_vehicle = browser.find_element_by_id("vehicle1")
        assert bike_vehicle.is_selected()

        car_vehicle = browser.find_element_by_id("vehicle2")
        assert not car_vehicle.is_enabled()

        boat_vehicle = browser.find_element_by_id("vehicle3")
        assert not boat_vehicle.is_selected()

        language = browser.find_element_by_id("css")
        assert language.is_selected()

    finally:
        time.sleep(5)
        browser.quit()
