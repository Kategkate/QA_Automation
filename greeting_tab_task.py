import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = 'https://arturmkr.github.io/simple_web_site/greeting.html'


def test_greeting_open_page_first_time():
    try:
        browser.get(link)
        time.sleep(10)
        button = browser.find_element_by_name("cname")
        button.click()
        # table_body = WebDriverWait(browser, 3).until(
            # EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#demo > tbody > tr >td:nth-child(2)"))
        # )
        alert = browser.switch_to.alert()
        name_input = alert.send_keys()
        alert.accept()
        message = name_input.text
        # cookies = {c["name"]: c["value"] for c in browser.get_cookies()}
        print(message)

    finally:
        browser.quit()
