from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Tests(TestCase):
    def test_hotline_searchBox(self):
        #arrange
        url = 'https://hotline.ua/'
        search_text = "Razer Basilisk Ultimate Black (RZ01-03170100-R3G1)"
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(60)

        #act
        browser.get(url)
        browser.find_element(by=By.ID, value='searchbox').send_keys(search_text)
        browser.find_element(by=By.ID, value='doSearch').click()

        #assert
        response = browser.find_element(by=By.CLASS_NAME, value='title__main').text
        assert search_text in response
        browser.close()

    def test_catalog_selected(self):
        #arrange
        url = 'https://hotline.ua/'
        search_text = "Дитячі товари"
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(60)

        #act
        browser.get(url)
        browser.find_element(by=By.CLASS_NAME, value='deti').click()
        response = browser.find_elements(by=By.CLASS_NAME, value="cell-12")[2].text
        
        #assert
        assert search_text in response
        browser.close()