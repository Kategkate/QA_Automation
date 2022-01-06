import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = 'https://arturmkr.github.io/simple_web_site/table.html'
browser.get(link)


def test_weather_in_sydney():
    try:
        sydney_button_click = browser.find_element_by_css_selector( "[type=button]:nth-child(4)" ).click()
        wait_response = WebDriverWait( sydney_button_click, 20 ).until(
            EC.presence_of_element_located( (By.ID, "sydney_button") )
        )
        sydney_time = browser.find_element_by_id( "demo_weather" )
        assert sydney_time == "h1"

    finally:
        time.sleep( 10 )
        browser.quit()
