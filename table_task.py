import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = 'https://arturmkr.github.io/simple_web_site/table.html'


def test_check_weather_info():
    try:
        browser.get(link)
        weather_info = browser.find_element_by_id("demo_weather")
        text = weather_info.get_attribute('innerText')
        assert text == "PENDING INFO ABOUT WEATHER..."

    finally:
        browser.quit()


def test_weather_in_sydney():
    try:
        browser.get(link)
        sydney_button_click = browser.find_element_by_css_selector("[type=button]:nth-child(4)")
        sydney_button_click.click()
        sydney_time = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#demo_weather > p:nth-child(3)"))
        )
        text = sydney_time.get_attribute('innerText')
        assert text == "Current time 01:23"

    finally:
        browser.quit()


def test_check_CD_collection_table_displayed():
    try:
        browser.get(link)
        collection_button = browser.find_element_by_css_selector("[type=button]:nth-child(5)")
        collection_button.click()
        cd_collection = browser.find_element_by_id("demo")
        assert cd_collection.is_displayed()

    finally:
        browser.quit()


def test_artists_order():
    try:
        browser.get(link)
        collection_button = browser.find_element_by_xpath("//*[.='Get my CD collection']")
        collection_button.click()
        artists_list_elements = WebDriverWait(browser, 2).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#demo > tbody > tr > td:nth-child(1)"))
        )

        actual_texts = []
        expected_texts = ["Bob Dylan", "Bonnie Tyler", "Dolly Parton", "Gary Moore", "Eros Ramazzotti", "Bee Gees"]

        for artist_el in artists_list_elements:
            actual_texts.append(artist_el.get_attribute('innerText'))

        assert actual_texts == expected_texts

    finally:
        browser.quit()


def test_songs_existence():
    try:
        browser.get(link)
        collection_button = browser.find_element_by_xpath("//*[.='Get my CD collection']")
        collection_button.click()
        artists_list_elements = WebDriverWait(browser, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#demo > tbody > tr > td:nth-child(2)"))
        )
        req_songs = []
        expected_songs_texts = ["Empire Burlesque", "Hide your heart"]

        for artist_el in artists_list_elements:
            req_songs.append(artist_el.get_attribute('innerText'))
        result = set(req_songs).intersection(expected_songs_texts)
        assert "Empire Burlesque" in req_songs
        assert "Hide your heart" in req_songs

    finally:
        browser.quit()


def test_table_rows_count():
    try:
        browser.get(link)
        collection_button = browser.find_element_by_xpath("//*[.='Get my CD collection']")
        collection_button.click()
        table_body = WebDriverWait(browser, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#demo > tbody > tr >td:nth-child(2)"))
        )

        assert len(table_body) == 6

    finally:
        browser.quit()



